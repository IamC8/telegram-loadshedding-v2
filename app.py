from flask import Flask, render_template, jsonify
from database import load_db


app = Flask(__name__)


@app.route("/")
def hello_world():
    tel = load_db()
    return render_template("home.html",
                           jobs=tel)

@app.route("/api")
def list_json():
    tel = load_db()
    return jsonify(tel)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

#  https://www.youtube.com/watch?v=yBDHkveJUf4
