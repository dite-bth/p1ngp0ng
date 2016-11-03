import pygame
import json
from gpiozero import Button

class gameLogic(object):
	global info
	redset = 0
	blueset = 0
	restart = False
	win = "none"
	winner = False
	redpoints = 0
	bluepoints = 0
	Buttonred = Button(19)
	Buttonblue = Button(21)
	Buttonreset = Button(23)
	player1 = "Player 1"
	player2 = "Player 2"
	global matchrunning
	matchrunning = True
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
	        #publish()
	        requests.get("http://localhost:5000/publish")

	          
	            
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

	        
	Buttonred.when_pressed = pointred
	Buttonblue.when_pressed = pointblue
