from flask import Flask
from flask import render_template
import gevent
from gevent.wsgi import WSGIServer
from gevent.queue import Queue
import sse
import requests

app = Flask(__name__)
subscriptions = []

@app.route('/')
def index():
    return "1"



@app.route("/publish")
def publish():
    #Send dummy data
    def notify():
        msg = '{"player1": "Linus",'\
            '"player2": "Masse",'\
            '"score": "(10, 0)"}'
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

