from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user
from form_fields import email_check, login_form
from db.models import Admin
from werkzeug.security import check_password_hash
from config import config_email

login = Blueprint('login', __name__,
static_folder='static', template_folder='templates', static_url_path='/static/login')
# generating login page
@login.route('/')
def index():
    form = login_form()
    return render_template('login.html', form=form)
#for authentication of user to access admin route
@login.post('/')
def login_check():
    form = login_form()
    password = request.form.get('password')
    remember = form.remember.data
    user = Admin.query.filter_by(email=form.email.data).first()
    if user:
        password_check = check_password_hash(user.password, password)
        if password_check:
            login_user(user, remember=remember)
            return redirect(url_for('admin.index'))
    flash('incorect password or email, \n please try again.', 'danger')
    return redirect(url_for('login.index'))
# for GET request by the client
@login.route('/recover')
def recover():
    form = email_check()
    return render_template('forgot_pw.html', form=form)
# this will check an authentication of the user
@login.post('/recover')
def recover_post():
    form = email_check()
    user = form.email.data
    if form.validate_on_submit:
        user = Admin.query.filter_by(email = user).first()
        if user:
            if user.email == config_email:
                flash(
                    "Oops! this email cannot be reset, please contact the app developers for getting the password",
                    "warning"
                )
            else:
                flash(
                    "the reset link will be sent on your email",
                    "success"
                )
        else:
            flash(
                "The email doesn't exist, please contact the app developers",
                "danger"
            )
            return redirect(url_for('login.recover'))
        return render_template('forgot_pw.html', form=form)
        