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

    username_or_email = request.form.get('username_or_email')
    password = request.form.get('password')

    if '@' in username_or_email:
        email = username_or_email
        user = crud.get_user_by_email(email)
    else:
        user_name = username_or_email
        user = crud.get_user_by_username(user_name)

    if user.password == password:
        flash(f"You are now logged in!")
        return render_template("login.html")

    else:
        flash(f"Sorry! The password you entered is incorrect.")
        return redirect('/')

    


if __name__=='__main__':
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)