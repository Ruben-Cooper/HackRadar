from logging import PlaceHolder
from flask import Blueprint, request, render_template
from .forms import RegisterForm, CreateEventForm, LoginForm
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    print(request.headers)
    print(request.args.get('name'))
    return render_template('base.html')


@bp.route('/create_event', methods=['GET', 'POST'])
@login_required  # Decorator to protect the route from unauthenticated users
def create_event():
    createform = CreateEventForm()
    if createform.validate_on_submit():
        print(f"Event Name: {createform.event_name.data}, Event Description: {createform.event_description.data}, Event Date: {createform.event_date.data}, Event Image: {createform.event_image.data}, Event Location: {createform.event_location.data}, Ticket Quantity: {createform.ticket_quantity.data}, Ticket Price: {createform.ticket_price.data}, Event Category: {createform.event_category.data}")
    return render_template('create_event.html', form=createform)


@bp.route('/booking_history')
@login_required
def booking_history():
    return render_template('booking_history.html')
