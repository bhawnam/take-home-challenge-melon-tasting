"""Server for melon reservations app."""

from flask import (Flask, render_template, redirect, request, session, flash)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from datetime import datetime, timedelta

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
        session['user'] = user.user_name
        flash(f"You are now logged in!")
        return render_template("login.html")

    else:
        flash(f"Sorry! The password you entered is incorrect.")
        return redirect('/')

    
@app.route('/all_reservations', methods=["POST"])
def tasting_reservations():
    """"View tasting reservations. """

    chosen_date = request.form.get('date')
    user_name = session['user']
    user = crud.get_user_by_username(user_name)

    is_reservation = crud.look_for_reservation(chosen_date, user)

    if is_reservation:
        flash(f"Sorry! You already have a reservation booked for this date. Choose a different date.")
        return redirect('/')

    chosen_start_time = request.form.get('start_time').split(":")
    chosen_end_time = request.form.get('end_time').split(":")

    if chosen_start_time[0]:
        start_time = datetime.now().replace(hour=int(chosen_start_time[0]), minute=int(chosen_start_time[1]))
    else:
        start_time = datetime.now().replace(hour=0, minute=0)
    
    time_delta = timedelta(minutes=30)

    if chosen_end_time[0]:
        end_time = datetime.now().replace(hour=int(chosen_end_time[0]), minute=int(chosen_end_time[1]))

    else:
        end_time = datetime.now().replace(hour=23, minute=30)
    
    slots_list = []
    while end_time > start_time:
        print(start_time.strftime("%H:%M"))
        slots_list.append(start_time.strftime("%H:%M"))
        start_time += time_delta
    
    return render_template('all_reservations.html', reservation_slots=slots_list, date=chosen_date)


@app.route('/book-reservation/<date>', methods=["POST"])
def reserve_tasting(date):
    """Book a reservation slot.  """

    chosen_date = date
    chosen_time = request.form.get('reservation_slots')
    user_name = session['user']

    user = crud.get_user_by_username(user_name)

    user_reservation = crud.create_reservation(chosen_date, chosen_time, user)

    if user_reservation:
        flash(f"Your booking is confirmed")
        return redirect('/user-reservations')

    else:
        flash(f'Oops! Something went wrong. Please try booking again.')
        return redirect('/')


@app.route('/user-reservations', methods=["GET","POST"])
def user_reservations():
    """View all user reservations. """
    
    user_name = session['user']
    user = crud.get_user_by_username(user_name)

    reservations = crud.get_all_user_reservations(user)

    return render_template('user_reservations.html', reservations=reservations)

    
if __name__=='__main__':
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)