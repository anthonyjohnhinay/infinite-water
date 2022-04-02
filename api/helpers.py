#helpers.py list of all needed tools


import random
import string
from datetime import datetime
from flask import render_template
from db.database import db
from db.models import *
from flask_mail import Mail, Message
"""
Initializing the mail thru the init_app(app) in app dir
"""
mail = Mail()
def gen_password():
    pw = []
    char = list(string.ascii_letters + string.digits)
    length = 8
    random.shuffle(char)
    for i in range(length):
        pw.append(random.choice(char))
    product = ("".join(pw))
    return product
# this uses in the form_field.py for the dynamic SelectField
def product_catalog():
    return Catalog.query
def customer_catalog():
    return Customer.query
"""
Function for sending email by email_reset(email.attr)
"""
def email_reset(user_email, user_name, pw):
    msg = Message(
        'Admin reset your password',
        sender='Infinity-flow',
        recipients = [user_email]

    )
    msg.html = render_template(
        'email/admin_reset.html',
        user = user_name,
        password = pw
    )
    mail.send(msg)
def user_reset(user):
    print(user)
    token = user.get_token()
    msg = Message(
        'Account password reset',
        sender='Infinity-flow',
        recipients=[user.email]
    )
    msg.html = render_template(
        'email/user_reset.html',
        token=token,
        user = user.user, email=user.email
    )
    mail.send(msg)

def create_user(email, username, pw):
    msg = Message('Account Creation',
    sender='Infinity-flow',
    recipients=[email],
    )
    msg.html = render_template('email/user_create.html', user = username, email=email, pw=pw)
    mail.send(msg)
    
def create_transaction_id(id):
    pass
