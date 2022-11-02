# import flask - from the package import class
from email.policy import default
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitedata.sqlite'
db.init_app(app)

bootstrap = Bootstrap5(app)

class User(db.Model):
    __tablename__ = 'usercredentials'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(9), nullable=False)
    address = db.Column(db.String(100), nullable=False)


class Event(db.Model):
    __tablename__ = 'eventdetails'
    event_id = db.Column(db.Integer, primary_key=True)
    event_creator = db.Column(db.String(100), nullable=False)
    event_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime.date, nullable=False)
    time = db.Column(db.DateTime.time, nullable=False)
    online = db.Column(db.Boolean, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    event_status = db.Column(db.String(50), nullable=False)
    tickets = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=False, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Booking(db.Model):
    __tablename__ = 'bookingdetails'
    booking_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tickets = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime.date, db.ForeignKey('event.id'), nullable=False)
    time = db.Column(db.DateTime.time, db.ForeignKey('event.id'), nullable=False)

class Comment(db.Model):
    __tablename__ = 'commentdetails'
    comment_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime.date, db.ForeignKey('event.id'), nullable=False)
    time = db.Column(db.DateTime.time, db.ForeignKey('event.id'), nullable=False)