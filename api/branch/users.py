
from flask import Blueprint, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from form_fields import *
from api.helpers import gen_password
from db.models import Admin
from db.database import db

api_users = Blueprint('api_users', __name__)

@api_users.post('/users/add')
def add_users_post():
    form = add_user()
    hashed_pw = gen_password()
    hashed_pw = generate_password_hash(hashed_pw, 'sha256')
    if form.validate_on_submit:
        users= Admin(email=form.email.data, user=form.username.data.title(), password=hashed_pw)
        db.session.add(users)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            flash('This user / admin is already exist!', 'danger')
            return redirect(url_for('admin.add_users'))
        flash('Succesfully add user', 'success')
        return redirect(url_for('admin.users'))



@api_users.route('/users/edit/<id>', methods=['POST', 'GET'])
def edit_users_post(id):
    form = add_user()
    update = Admin.query.filter_by(id=id).update(dict( user = form.username.data, email = form.email.data))
    print(update)
    db.session.commit()
    flash('Succesfully edited the user!', 'success')
    return redirect(url_for('admin.users'))
@api_users.get('/users/delete/<id>')
def delete_users(id):
    user = Admin.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Succefully delted the user', 'success')
    return redirect (url_for('admin.users'))