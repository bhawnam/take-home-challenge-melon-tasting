"""CRUD operations. """

from model import db, User, Reservations, connect_to_db

def create_user(first_name, last_name, user_name, email, passsword):

    user = User(first_name= first_name, last_name= last_name, user_name= user_name, email= email, passsword= passsword)
    db.session.add(user)
    db.session.commit()

    return user    


def create_reservation(date, time, user):

    reservation = Reservations(reservation_date= date, reservation_time= time, user= user)
    db.session.add(reservation)
    db.session.commit()
    
    return reservation


def get_user_by_email(email):

    user = User.query.filter_by(email=email).first()
    return user


def get_user_by_username(username):

    user = User.query.filter_by(user_name=username).first()
    return user


def look_for_reservation(date, user):

    is_reservation = Reservations.query.filter((Reservations.reservation_date==date) & (Reservations.user==user)).first()
    return is_reservation

def get_all_user_reservations(user):

    reservations = Reservations.query.filter_by(user=user).all()
    return reservations

if __name__=='__main__':
    from server import app
    connect_to_db(app)