from flask import Flask, render_template, jsonify, request
from database import load_db
from forms import *


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

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        db = MySQLdb.connect(user="root", passwd="", db="cs324", host="127.0.0.1")
        c=db.cursor()
        c.executemany('''select * from student where name = %s''', request.form['search'])
        for r in c.fetchall():
            print r[0],r[1],r[2]
            return redirect(url_for('search'))
    return render_template('search.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

#  https://www.youtube.com/watch?v=yBDHkveJUf4
