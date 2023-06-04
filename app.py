from flask import Flask, render_template, jsonify, request
from database import load_db
from forms import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/api")
def list_json():
    tel = load_db()
    return jsonify(tel)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        req = request.form
        input = req["area"]
        res = load_db(input)
        # for r in res:
        #     print(r)
        return render_template('home.html', results=res)
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

#  https://www.youtube.com/watch?v=yBDHkveJUf4
# <tr onclick="window.open('https://t.co/' + {{ res['id'] }})">
