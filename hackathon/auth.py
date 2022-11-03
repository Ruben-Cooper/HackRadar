from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
#from .models import User
from .forms import LoginForm, RegisterForm
from flask_login import UserMixin, current_user, login_user, login_required, logout_user
from .models import User
from . import db

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    regform = RegisterForm(csrf_enabled=False)
    if regform.validate_on_submit():
        user = User(username=regform.user_name.data,
                    email=regform.email_id.data, contactnumber=regform.contact_number.data, address=regform.address.data)
        user.set_password(regform.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=regform)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm(csrf_enabled=False)
    if (loginform.validate_on_submit):
        user = User.query.filter_by(
            username=loginform.loginusername.data).first()
        # If username exists and then tests password
        if user and user.check_password(loginform.loginpassword.data):
            login_user(user)

        return render_template('SignIn.html', form=loginform)


# @bp.route('/login', methods=['GET', 'POST'])
# def authenticate():  # view function
#     print('In Login View function')
#     login_form = LoginForm()
#     error = None
#     if (login_form.validate_on_submit() == True):
#         user_name = login_form.username.data
#         password = login_form.password.data
#         u1 = User.query.filter_by(name=user_name).first()
#         if u1 is None:
#             error = 'Incorrect user name'
#         # takes the hash and password
#         elif not check_password_hash(u1.password_hash, password):
#             error = 'Incorrect password'
#         if error is None:
#             login_user(u1)
#             # this gives the url from where the login page was accessed
#             nextp = request.args.get('next')
#             print(nextp)
#             if next is None or not nextp.startswith('/'):
#                 return redirect(url_for('index'))
#             return redirect(nextp)
#         else:
#             flash(error)
#     return render_template('user.html', form=login_form, heading='Login')
