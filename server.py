"""Server for melon reservations app."""

from flask import (Flask, render_template, redirect, request, session, flash)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "takehomechallenge"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage. """

    return render_template("homepage.html")


@app.route('/login', methods=["POST"])
def login():
    """View login page. """

    return render_template("login.html")


if __name__=='__main__':
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)