
from flask import Blueprint, render_template, redirect, url_for, flash, request
from form_fields import *
admin = Blueprint('admin', __name__,
static_folder='static', template_folder='templates', static_url_path='/static/admin')

@admin.route('/')
def index():
    return render_template('dashboard.html')
@admin.route('/users')
def users():
    form = add_user()
    return render_template('manage_user.html' ,form=form)
@admin.post('/users')
def users_post():
    
    email = request.form['email']
    name = request.form['username']
    role = request.form['role']

    print(name, email, role)
    
    return redirect( url_for('admin.users'))