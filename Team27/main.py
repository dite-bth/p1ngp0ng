# coding=utf-8

from flask import Flask, render_template, request, Response
from flask import redirect
import requests
from flask_cors import CORS, cross_origin
import json

import time
import gevent
from gevent.wsgi import WSGIServer
from gevent.queue import Queue
from sse import ServerSentEvent
#from gameLogic import gameLogic
app = Flask(__name__)
CORS(app)

subscriptions = []



@app.route("/")                                                                     #Visar att detta är rootsidan.
def index():
    return render_template("start.html")                                            #Här kan man lägga in url för att skicka till annan sida.

@app.route("/publish")
def publish():
    #Send dummy data
    def notify():
        info = [{'Redpoints': "redpoints",
             'Bluepoints' : "bluepoints",
             'Winner' : "win",
             'Redset' : "redset",
             'Blueset' : "blueset",
             'blueplayer' : "player2",
             'matchstart' : "matchrunning"
           }]
        for sub in subscriptions[:]:
            sub.put(json.dumps(info[0]))
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

@app.route('/playgame')
def playgame():
    return render_template('gameplay.html')

if __name__ == "__main__":
    app.debug = True
    server = WSGIServer(("127.0.0.1", 5000), app)
    server.serve_forever()
