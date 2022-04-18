
from flask import Blueprint, jsonify, request

from assets.form_fields import transaction

"""
This route is only used for the interaction between the database and the users (POST) request
"""
api = Blueprint('api', __name__)

"""
We nested the routes to minimize the contents and organize all
"""
from .branch.products import api_product
api.register_blueprint(api_product, url_prefix='/products')

from .branch.users import api_users
api.register_blueprint(api_users, url_prefix="/users")

from .branch.customers import api_customer
api.register_blueprint(api_customer, url_prefix='/customers')

from .branch.transaction import api_transaction
api.register_blueprint(api_transaction, url_prefix='/transaction')

from .branch.silent import api_silent
api.register_blueprint(api_silent, url_prefix='/silent')


#parent process for verfication
from db.models import *
from werkzeug.security import check_password_hash
@api.post('/verify')
def user_verify():
    id = request.form['id']
    email= request.form['email']
    pw = request.form['password']
    user = db.session.query(Admin).filter((Admin.email==email) | (Admin.user == email)).first()
    if user:
        password_check = check_password_hash(user.password, pw)
        if password_check:
            return jsonify({
                'title' : 'Success',
                'identifier' : 'success',
                'info' : 'Succesfully Authenticated the transaction'
                })
    return jsonify({
            'title' : 'Forbidden',
            'identifier' : 'warning',
            'info' : 'Wrong credentials, please try again. '
            })
    