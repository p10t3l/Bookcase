from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder="static")


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/add_book")
def add_book():
    return render_template('add_book.html')


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
