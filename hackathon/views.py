from logging import PlaceHolder
from flask import Blueprint, request, render_template
from .forms import RegisterForm, CreateEventForm, LoginForm
from flask import Flask, render_template, request, redirect, url_for


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
    return render_template('register.html', form=regform)

@bp.route('/create_event', methods=['GET', 'POST'])
def create_event():
    createform = CreateEventForm()
    if createform.validate_on_submit():
        print(f"Event Name: {createform.event_name.data}, Event Description: {createform.event_description.data}, Event Date: {createform.event_date.data}, Event Image: {createform.event_image.data}, Event Location: {createform.event_location.data}, Ticket Quantity: {createform.ticket_quantity.data}, Ticket Price: {createform.ticket_price.data}, Event Category: {createform.event_category.data}")
    return render_template('create_event.html', form=createform)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        print(f"Username: {loginform.loginusername.data}, Password: {loginform.loginpassword.data}")
    return render_template('SignIn.html', form=loginform)

@bp.route('/booking_history')
def booking_history():
    return render_template('booking_history.html')