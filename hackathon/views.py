from logging import PlaceHolder
from flask import Blueprint, request, render_template
from .forms import RegisterForm, CreateEventForm, LoginForm, BookEventForm
from flask import Flask, render_template, request, redirect, url_for
from .db import db, User, Event


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    print(request.headers)
    print(request.args.get('name'))
    return render_template('base.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    regform = RegisterForm()
    if regform.validate_on_submit():
        print(f"Username: {regform.user_name.data}, Email: {regform.email_id.data}, Password: {regform.password.data}, Contact Number: {regform.contact_number.data}, Address: {regform.address.data}")
        user = User(username=regform.user_name.data,
                    email=regform.email_id.data)
        user.set_password(regform.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=regform)


@bp.route('/create_event', methods=['GET', 'POST'])
def create_event():
    createform = CreateEventForm()
    if createform.validate_on_submit():
        print(f"Event Name: {createform.event_name.data}, Event Description: {createform.event_description.data}, Event Date: {createform.event_date.data}, Event Image: {createform.event_image.data}, Event Location: {createform.event_location.data}, Ticket Quantity: {createform.ticket_quantity.data}, Ticket Price: {createform.ticket_price.data}, Event Category: {createform.event_category.data}")
        event = Event(event_name=createform.event_name.data,
                      description=createform.event_description.data,
                      date=createform.event_date.data,
                      image=createform.event_image.data,
                      online=createform.online_event.data,
                      location=createform.event_location.data,
                      category=createform.event_category.data,
                      status = createform.event_status.data,
                      ticket_amt=createform.ticket_quantity.data,
                      price=createform.ticket_price.data)
        db.session.add(event)
        db.session.commit()

    
    return render_template('create_event.html', form=createform)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        print(
            f"Username: {loginform.loginusername.data}, Password: {loginform.loginpassword.data}")
    return render_template('SignIn.html', form=loginform)


@bp.route('/booking_history')
def booking_history():
    return render_template('booking_history.html')

@bp.route('/event/', methods=['GET', 'POST'])
def event_details():
    bookform = BookEventForm()
    if bookform.validate_on_submit():
        print(f"Ticket Quantity: {bookform.ticket_quantity.data}")
    return render_template('view_event.html', form=bookform)
