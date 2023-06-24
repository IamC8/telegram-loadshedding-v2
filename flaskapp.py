from flask import Flask, render_template, request
from database import load_db
from forms import *

app = Flask(__name__)


@app.route("/")
def myhome1():
    return render_template("home.html")


@app.route("/home")
def myhome2():
    return render_template("home.html")


@app.route("/about")
def myabout():
    return render_template("about.html")


@app.route("/help")
def myhelp():
    return render_template("help.html")


@app.route('/search', methods=['GET', 'POST'])
def mysearch():
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
    app.run(host='0.0.0.0', debug=False)

#  https://www.youtube.com/watch?v=yBDHkveJUf4
# <tr onclick="window.open('https://t.co/' + {{ res['id'] }})">
