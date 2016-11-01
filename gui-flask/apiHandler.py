
from flask import render_template, Flask

import requests

app = Flask(__name__)
@app.route('/users/')
def users():
    req = requests.get('https://api.github.com/events')
    return req


if __name__ == "__main__":
    app.run()