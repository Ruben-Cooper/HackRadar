from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from .forms import LoginForm, RegisterForm, CreateEventForm
from flask_login import current_user, login_user, login_required, logout_user
from .models import User, Event, Booking
from . import db
from sqlalchemy import desc, asc

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    regform = RegisterForm()
    if regform.validate_on_submit():
        user = User(username=regform.user_name.data,
                    email=regform.email_id.data, contactnumber=regform.contact_number.data, address=regform.address.data)
        user.set_password(regform.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=regform)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(
            username=loginform.loginusername.data).first()
        if user is None or not user.check_password(loginform.loginpassword.data):
            flash("Invalid username or password")
            return redirect(url_for('auth.login'))
        login_user(user, loginform.RememberMe.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template('SignIn.html', title='Sign In', form=loginform)


@bp.route('/user/<username>')
@login_required
def userpage(username):
    user = current_user  # Get the current user
    user = User.query.filter_by(username=user.username).first()
    bookings = Booking.query.filter_by(user_id=user.id).order_by(asc(Event.date)).all()
    events = Event.query.filter_by(user_id=user.id).order_by(asc(Event.date)).all()
    if events is None:
        events = []
    return render_template('userpage.html', user=user, events=events, bookings=bookings, event_name=event_name, status=status)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


# @bp.route("/user/edit/<int:event_id>")
# def edit_event(event_id):
#     form = CreateEventForm()
#     form.validate():
#     query = CreateEventForm(form.event_name.data, form.event_description.data, form.event_date.data, form.online_event.data, form.event_location.data, form.event_category.data, form.event_status.data, form.ticket_quantity.data, form.ticket_price)

#     return render_template("edit_event.html", form=form)
