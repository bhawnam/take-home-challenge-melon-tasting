"""Models for melon reservations app. """

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy()

class User(db.Model):
    """A user. """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement= True, primary_key= True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    user_name = db.Column(db.String, nullable= False, unique = True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    # reservations = a list of Reservation object

    def __repr__(self):
        return f'<User iser_id={self.user_id} user_name={self.user_name}>'


class Reservations(db.Model):
    """Reservations. """

    __tablename__ = "reservations"

    reservation_id = db.Column(db.Integer, autoincrement= True, primary_key= True)
    reservation_date = db.Column(db.DateTime)
    reservation_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    is_cancelled = db.Column(db.Boolean, default= False)

    user = db.relationship('User', backref='reservations')
     
    def __repr__(self):
        return f'<Reservation reservation_id={self.reservation_id} reservation_date={self.reservation_date}>'


def connect_to_db(flask_app, db_uri='postgresql:///melon_reservations', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the DB!')


if __name__== "__main__":
    from server import app

    connect_to_db(app)
