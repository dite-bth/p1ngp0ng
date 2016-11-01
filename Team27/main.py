# coding=utf-8
import pymysql.cursors
from flask import Flask, render_template, request
from flask import redirect
#from gpiozero import Button
import json
import simplejson as json
import pygame
import time
import gevent
from gevent.wsgi import WSGIServer
from gevent.queue import Queue
from sse import ServerSentEvent

app = Flask(__name__)

global info
redset = 0
blueset = 0
restart = False
win = "none"
winner = False
redpoints = 0
bluepoints = 0
#Buttonred = Button(19)
#Buttonblue = Button(21)s
#Buttonreset = Button(23)
player1 = ""
player2 = ""
global matchrunning
matchrunning = True

@app.route("/")                                                                     #Visar att detta är rootsidan.
def index():
    return render_template("start.html")                                            #Här kan man lägga in url för att skicka till annan sida.


@app.route("/register/", methods = ["POST"])                                        #Denna def får fram och visar vad nicknacmet för det scannade kortet är
def hej():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='apa',
                             db='user',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    try:
        kod = request.form['usr_name']
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id` FROM `players` WHERE `id`=%s"
            cursor.execute(sql, (kod,))
            result = cursor.fetchone()

        if not result:
            return redirect('/registrering_pingponghack?id='+kod)
        else:
            with connection.cursor() as cursor:
                kodOne = "SELECT `id` FROM `players` WHERE `id`=%s"                 #Jämför med databasen ifall scannade ID:t på kortet finns i databasen
                kodRes = cursor.execute(kodOne, (kod,))

                if kodRes:
                    with connection.cursor() as cursor:
                        global resultTwo
                        kodTwo = "SELECT `nickname` FROM `players` WHERE `id`=%s"   #Tar reda på nicknamet till ID:t i databasen
                        kodTwoRes = cursor.execute(kodTwo, (kod,))
                        resultTwo = cursor.fetchone()
                        print(resultTwo)                                            #Printar nicknamet till konsolen
                        info = [{'redplayer' : resultTwo,}]
                        with open('info2.txt', 'w') as outfile:
                            json.dump(info,outfile)
                else:
                    print("attans rabarber")
                return redirect('/')
    
    finally:
        connection.close()
        
info = [{'matchstart' : matchrunning}]
with open('info.txt', 'w') as outfile:
    json.dump(info,outfile)

def startmatch(name1, name2):
    global player1, player2, matchrunning
    player1 = name1
    player2 = name2
    matchrunning = True
    
def Buttonreset():
    redpoints = 0
    bluepoints = 0
    winner = False
    win = "none"
    restart = False
    redset = 0
    blueset = 0

def pointred():
    global redpoints
    global winner
    global restart
    global bluepoints
    global win
    global redset
    global blueset



    redpoints = redpoints + 1
    dump()
    
    if (redpoints >= 11) and (redpoints - bluepoints >= 2) and (winner == False):
        if (redset < 1):
            redset += 1
            bluepoints = 0
            redpoints = 0
            print("Red has won a set!")
            
            dump()

            print("New set!")
            
        else :
            print("You have won the match, player red!")

            win = "red";
            pygame.init()
            pygame.mixer.init()
            sounda= pygame.mixer.Sound("klappklapp.wav")
            sounda.play()
            pygame.mixer.quit()

            
            redset = 2
            
            dump()

            time.sleep (4)
            winner = True

    elif (winner == True) and (restart == False):
        redpoints -= 1
        print("Press a button again to restart.")

        restart = True

    elif (restart == True):
        redpoints = 0
        bluepoints = 0
        winner = False
        win = "none"
        restart = False
        redset = 0
        blueset = 0
    else:
        print("Player red has " + str(redpoints) + " points!")

          
            
def pointblue():
    global winner
    global restart
    global bluepoints
    global redpoints
    global win
    global redset
    global blueset

    bluepoints = bluepoints + 1
    dump()
    
    if (bluepoints >= 11) and (bluepoints - redpoints >= 2) and (winner == False):
        if (blueset < 1):
                blueset += 1
                bluepoints = 0
                redpoints = 0
                print("Blue has won a set!")

                dump()

                print("New set!")

        else:
            print("You have won the match, player blue!")

            win = "blue";
            pygame.init()
            pygame.mixer.init()
            sounda= pygame.mixer.Sound("klappklapp.wav")
            sounda.play()
            pygame.mixer.quit()

            blueset = 2
            dump()
            
            time.sleep (4)            

            winner = True
            
    elif (winner == True) and (restart == False):
        bluepoints -= 1
        print("Press a button again to restart.")

        restart = True

    elif (restart == True):
        redpoints = 0
        bluepoints = 0
        winner = False
        win = "none"
        restart = False
        redset = 0
        blueset = 0

    else:
        print("Player blue has " + str(bluepoints) + " points!")



def dump():
    
    info = [{'Redpoints': redpoints,
             'Bluepoints' : bluepoints,
             'Winner' : win,
             'Redset' : redset,
             'Blueset' : blueset,

             'blueplayer' : player2,
             'matchstart' : matchrunning
           }]
    with open('info.txt', 'w') as outfile:
        json.dump(info,outfile) 

        
#Buttonred.when_pressed = pointred
#Buttonblue.when_pressed = pointblue

@app.route("/registrering_pingponghack")
def registrering_pingponghack():
    kod = request.args.get("id")
    return render_template("registrering_pingponghack.html", kod_variable=kod)


@app.route("/publish")
def publish():
    #Send dummy data
    def notify():
        msg = "{'Redpoints': %s,\
              'Bluepoints' : %s,\
              'Winner' : %s,\
              'Redset' : %s,\
              'Blueset' : %s,\
              'blueplayer' : %s,\
              'matchstart' : %s\
                }" % redpoints, bluepoints, win, redset, blueset, player1, player2, matchrunning
        for sub in subscriptions[:]:
            sub.put(msg)

    gevent.spawn(notify)
    return "OK"


@app.route("/subscribe")
def subscribe():
    def gen():
        q = Queue()
        subscriptions.append(q)
        try:
            while True:
                result = q.get()
                ev = ServerSentEvent(str(result))
                yield ev.encode()
        except GeneratorExit:  # Or maybe use flask signals
            subscriptions.remove(q)

    return Response(gen(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.debug = True
    server = WSGIServer(("0.0.0.0", 5000), app)
    server.serve_forever()










