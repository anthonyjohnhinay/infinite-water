
from flask import Blueprint, jsonify, redirect, request, url_for, flash
from flask_security import hash_password
from werkzeug.security import generate_password_hash
from assets.form_fields import *
from api.helpers import *
from db.models import Admin
from db.database import db

api_silent = Blueprint('api_silent', __name__)

@api_silent.post('/')
def fetch_account():
    user_id = request.form['id']
    if user_id == '1':
        return jsonify({
            'identifier' : 'error',
            'error' : 'this email cannot be reset'
        })
    user = Admin.query.filter_by(id=user_id).first()
    return jsonify({
        'identifier' : 'success',
        'id' : user.id,
        'email' : user.email,
        'username' : user.user
    })

@api_silent.post('/pw')
def fetch_password():
    user_id = request.form['id']
    user = Admin.query.filter_by(id=user_id).first()
    return jsonify({
        'identifier' : 'success',
        'email'    : user.email,
        'password' : user.password
    })


@api_silent.post('/filter')
def filter_request():
    search_param = request.form['params']
    search = Admin.query.filter_by()


@api_silent.post('/edit')
def after_request():
    user_id = request.form['id']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    if user_id == '1':
        return jsonify({
            'title' : 'Forbidden',
            'error' : 'This email cannot be edited',
            'identifier' : 'error'
        })
    hash_pw = generate_password_hash(password, 'sha256')
    update = Admin.query.filter_by(id=user_id).update(dict( user = username, email = email, password=hash_pw))
    try:
        db.session.commit()
    finally:
       db.session.close()
    return jsonify({
        'title' : 'Success!',
        'success' : f'{username} has been edited',
        'identfier' : 'success'
    })
@api_silent.post('/changepassword')
def change_pw_user():
    user_id = request.form['id']
    password = request.form['password']
    if user_id == '1':
        return jsonify({
            'title' : 'Forbidden',
            'msg' : 'This email cannot be edited',
            'identifier' : 'danger'
        })
    hash_pw = generate_password_hash(password, 'sha256')
    update = Admin.query.filter_by(id=user_id).update(dict( password=hash_pw))
    try:
        db.session.commit()
    finally:
       db.session.close()
    return jsonify({
        'title' : 'Success!',
        'msg' : f'Succefully change password!',
        'identfier' : 'success'
    })
@api_silent.post('/add')
def add_acount():
    username = request.form['username']
    email = request.form['email']
    raw_password = request.form['raw_password']
    hash_password = request.form['hash_password']
    print(raw_password)
    if raw_password == "":
        raw_password = hash_password
    else:
        raw_password = generate_password_hash(raw_password, 'sha256')
    print(raw_password)
    user = Admin(email=email, user=username, password=raw_password)
    db.session.add(user)
    try:
        db.session.commit()
    except:
        return jsonify({'error': 'The user is already exist.'})
    finally:
        db.session.close()
    return jsonify({'success': 'User has been added!'})