from .forms import RegisterForm, CreateEventForm, LoginForm, BookEventForm, CommentForm
from flask import Flask, render_template, request, redirect, url_for, abort, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, login_required, logout_user
from . import db
from .models import User, Event

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    print(request.headers)
    print(request.args.get('name'))
    return render_template('base.html')


@bp.route('/create_event', methods=['GET', 'POST'])
@login_required  # Decorator to protect the route from unauthenticated users
def create_event():
    form = CreateEventForm()
    if request.method == 'POST' and form.validate():
        new_event = Event(event_name=form.event_name.data, description=form.event_description.data, date=form.event_date.data, online=form.online_event.data, location=form.event_location.data,
                          category=form.event_category.data, status=form.event_status.data, tickets_amt=form.ticket_quantity.data, price=form.ticket_price.data, image=form.event_image.data, user_id=current_user.id)
        db.session.add(new_event)
        db.session.commit()
    return render_template('create_event.html', form=form)


@bp.route('/event/', methods=['GET', 'POST'])
def event_details():
    bookform = BookEventForm()
    commentform = CommentForm()
    if bookform.validate_on_submit():
        print(f"Ticket Quantity: {bookform.ticket_quantity.data}")
    return render_template('view_event.html', bookingform=bookform, commentforms=commentform)


@bp.route('/category/businesscase')  # this one
def business_case():
    return render_template('cate_businesscase.html')


@bp.route('/category/businessprop')
def business_prop():
    return render_template('cate_businessprop.html')


@bp.route('/category/codingcompetition')
def coding_competition():
    return render_template('cate_codingcomp.html')


@bp.route('/category/datathon')
def datathon():
    return render_template('cate_datathon.html')


@bp.route('/category/hackathon')
def hackathon():
    return render_template('cate_hackathon.html')


@bp.route('/category/ideapitch')
def idea_pitch():
    return render_template('cate_ideapitch.html')


@bp.route('/category/robotics')
def robotics():
    return render_template('cate_robotics.html')


@bp.route('/category/seminar')
def seminar():
    return render_template('cate_seminar.html')  # this one


@bp.errorhandler(400)
def page_not_found(e):
    return render_template('error.html'), 404


@bp.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html'), 500


@bp.errorhandler(403)
def forbidden(e):
    return render_template('error.html'), 403


@bp.errorhandler(410)
def gone(e):
    return render_template('error.html'), 410
