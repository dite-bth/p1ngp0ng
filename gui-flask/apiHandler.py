
from flask import render_template, Flask, request, redirect

import config
import json

app = Flask(__name__)
@app.route('/users/<card_id>')
def users(card_id):
    query = "SELECT * FROM user WHERE cardID=%s"
    config.cur.execute(query, (card_id,))
    res = config.cur.fetchall()
    json_result = {
        "name" : res[0][1],
        "card_id": res[0][2],
        "wins": res[0][3],
        "losses": res[0][4],
        "totalgames": res[0][5]
    }
    return json.dumps(json_result)

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form["name"]
        card_id = request.form["card_id"]
        query = "INSERT INTO user (name, cardID) VALUES (%s, %s)"
        config.cur.execute(query, (name, card_id))
        config.db.commit()
        print(query)
        return "Registration successful"
    else: 
        return "nej"




if __name__ == "__main__":
    app.run(debug = True)
