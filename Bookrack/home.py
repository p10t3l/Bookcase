from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder="static")


@app.route("/home")
def home():
    return render_template('home.html')


tasks = [
    "Chemia śmierci",
    "Zapisane w kościach"
]


@app.route("/add_book", methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        tasks.append(request.form['task'])

    return render_template('add_book.html', tasks=tasks)


@app.route("/przeczytane")
def read():
    return render_template('404.html')


@app.route("/nie_przeczytane")
def unread():
    return render_template('404.html')


@app.route("/do_kupienia")
def to_buy():
    return render_template('404.html')


@app.route("/404")
def error():
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)
