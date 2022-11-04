from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, login_required, logout_user
from .models import User
from . import db

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
        login_user(user, False)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.index")
        return redirect(next_page)
    return render_template('SignIn.html', title='Sign In', form=loginform)


def logout():
    logout_user()
    return redirect(url_for('main.index'))
