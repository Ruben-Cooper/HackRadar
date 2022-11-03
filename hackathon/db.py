# import flask - from the package import class
from email.policy import default
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
# this is the name of the module/package that is calling this app
app = Flask(__name__)
app.debug = True
# set the app configuration data
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # to supress warning
# initialize db with flask app





class User(db.Model):
    __tablename__ = 'usercredentials'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    bookings = db.relationship('Booking', backref='user', lazy='dynamic')


class Event(db.Model):
    __tablename__ = 'eventdetails'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    online = db.Column(db.Boolean, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    tickets_amt = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=False, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')


class Booking(db.Model):
    __tablename__ = 'bookingdetails'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tickets = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, db.ForeignKey(
        'event.id'), nullable=False)
    time = db.Column(db.DateTime, db.ForeignKey(
        'event.id'), nullable=False)


class Comment(db.Model):
    __tablename__ = 'commentdetails'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(
        db.String(100), db.ForeignKey('user.id'), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, db.ForeignKey(
        'event.id'), nullable=False)
    time = db.Column(db.DateTime, db.ForeignKey(
        'event.id'), nullable=False)
