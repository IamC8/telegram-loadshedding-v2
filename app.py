from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS =[
    {'id': 1,
     'title': 'Main',
     'location': 'Johannesburg',
     'salary': "R1000"},
    {'id': 2,
     'title': 'Manager',
     'location': 'Johannesburg',
     'salary': "R1000"},
    {'id': 3,
     'title': 'Secretary',
     'location': 'Johannesburg',
     'salary': "R1000"},
    {'id': 4,
     'title': 'Claener',
     'location': 'Johannesburg',
     'salary': "R1000"},
    {'id': 5,
     'title': 'Parttner',
     'location': 'Johannesburg',
     'salary': "R1000"},
]

@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS)

@app.route("/api")
def list_json():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

#  https://www.youtube.com/watch?v=yBDHkveJUf4
