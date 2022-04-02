from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user
from flask_security import ResetPasswordForm
from assets.form_fields import *
from db.models import Admin
from db.database import db
from werkzeug.security import check_password_hash, generate_password_hash
from assets.configs import config_email
from api.helpers import user_reset

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
                user_reset(user)
                flash(
                    "the reset link will be sent on your email",
                    "success"
                )
                return redirect(url_for('login.index'))
        else:
            flash(
                "The email doesn't exist, please contact the app developers",
                "danger"
            )
            return redirect(url_for('login.recover'))
        return render_template('forgot_pw.html', form=form)

@login.route('/recover/<token>')
def reset_token(token):
    user = Admin.verify_reset_token(token)
    form = ResetPasswordForm()
    print('reset token success')
    if user is None:
        flash('The given link was expired please generate a new one.', 'warning')
        return redirect(url_for('login.index'))
    
    if form.validate_on_submit():
        print('success')
        hash_pw = generate_password_hash(form.password.data, 'sha256')
        user.password = hash_pw
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login.index'))
    return render_template('reset.html', form=form)