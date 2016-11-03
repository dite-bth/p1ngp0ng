from flask import Flask
from flask import render_template, Response, Request
import gevent
from gevent.wsgi import WSGIServer
from gevent.queue import Queue
from sse import ServerSentEvent

app = Flask(__name__)
subscriptions = []


@app.route('/screen')
def users():
	return render_template('screen.html')

@app.route("/publish")
def publish():
    #Send dummy data
    def notify():
        msg = '{"player1": "Linus",'\
            '"player1score": "10",'\
            '"player2": "Masse",'\
            '"player2score": "9"}'
        for sub in subscriptions[:]:
            sub.put(msg)

    gevent.spawn(notify)
    return "OK"

@app.route('/playgame')
def playgame():
	return render_template('index.html')

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
    server = WSGIServer(("0.0.0.0", 5000), app)
    server.serve_forever()
    app.debug = True

