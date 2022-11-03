# import flask - from the package import class
from email.policy import default
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def load_user(user_id):
        return User.query.get(int(user_id))


class Event(db.Model):
    __tablename__ = 'event'
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


class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tickets = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, db.ForeignKey('event.id'), nullable=False)
    time = db.Column(db.DateTime, db.ForeignKey('event.id'), nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(100),
                         db.ForeignKey('user.id'),
                         nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, db.ForeignKey('event.id'), nullable=False)
    time = db.Column(db.DateTime, db.ForeignKey('event.id'), nullable=False)
