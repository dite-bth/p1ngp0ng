
from flask import render_template, Flask, request, redirect
from flask_cors import CORS, cross_origin
import config
import json

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})
@app.route('/users/<card_id>')
def users(card_id):
    query = "SELECT cardID FROM user WHERE cardID=%s"
    config.cur.execute(query, (card_id,))
    res = config.cur.fetchall()
    for i in res:

        if i[0] == card_id:
            query2 = "SELECT * FROM user WHERE cardID=%s"
            config.cur.execute(query2, (card_id,))
            res2 = config.cur.fetchall()
            json_result = {
             "name" : res2[0][1],
                "card_id": res2[0][2],
                "wins": res2[0][3],
                "losses": res2[0][4],
                "totalgames": res2[0][5]
            }
            return json.dumps(json_result)
    return "null"


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
        return "null"




if __name__ == "__main__":
    app.run(debug = True, host='193.11.185.238')
