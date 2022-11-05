from .forms import RegisterForm, CreateEventForm, LoginForm, BookEventForm, CommentForm
from flask import Flask, render_template, request, redirect, url_for, abort, Blueprint, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, login_required, logout_user
from . import db
from .models import User, Event
from werkzeug.utils import secure_filename
import os
from sqlalchemy import desc, asc

bp = Blueprint('main', __name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/')
def index():
    print(request.headers)
    print(request.args.get('name'))
    return render_template('base.html')


@bp.route('/create_event', methods=['GET', 'POST'])
@login_required # Decorator to protect the route from unauthenticated users
def create_event():
    form = CreateEventForm()
    if request.method == 'POST' and form.validate():
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.path.abspath(os.path.dirname(
                __file__)), 'static/userimg', secure_filename(file.filename)))
            new_event = Event(event_name=form.event_name.data, description=form.event_description.data, date=form.event_date.data, online=form.online_event.data, location=form.event_location.data,
                              category=form.event_category.data, status=form.event_status.data, tickets_amt=form.ticket_quantity.data, price=form.ticket_price.data, image=filename, user_id=current_user.id)
            db.session.add(new_event)
            db.session.commit()
            return redirect(url_for('main.index', name=filename))
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
    category = Event.query.filter_by(category='Business Case Competition').order_by(asc(Event.date)).all()
    return render_template('cate_businesscase.html', category=category)


@bp.route('/category/businessprop')
def business_prop():
    category = Event.query.filter_by(category='Business Proposal').order_by(asc(Event.date)).all()
    return render_template('cate_businessprop.html', category=category)


@bp.route('/category/codingcompetition')
def coding_competition():
    return render_template('cate_codingcomp.html')


@bp.route('/category/Datathon')
def datathon():
    category = Event.query.filter_by(category='Datathon').order_by(asc(Event.date)).all()
    return render_template('cate_datathon.html', category=category)


@bp.route('/category/hackathon')
def hackathon():
    category = Event.query.filter_by(category='Hackathon').order_by(asc(Event.date)).all()
    return render_template('cate_hackathon.html', category=category)


@bp.route('/category/ideapitch')
def idea_pitch():
    category = Event.query.filter_by(category='Idea Pitch').order_by(asc(Event.date)).all()
    return render_template('cate_ideapitch.html', category=category)


@bp.route('/category/robotics')
def robotics():
    category = Event.query.filter_by(category='Robotics').order_by(asc(Event.date)).all()
    return render_template('cate_robotics.html', category=category)


@bp.route('/category/seminar')
def seminar():
    category = Event.query.filter_by(category='Seminar').order_by(asc(Event.date)).all()
    return render_template('cate_seminar.html', category=category)  


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
