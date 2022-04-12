from flask import Flask
from api.helpers import customer_catalog, product_catalog
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, EmailField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
"""
Validators - are the checkers whether the form is submitted
EmailField - Email forms in html
StringField - Regular forms in html
BooleanField - are usuallly check (true) and if not false
SubmitField - are the regular submit button 

to use import the file name then you can use * to import all or specified by 
the class name itself.
"""
class login_form(FlaskForm):
    email = EmailField('Name', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField()
class reset_form(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_pw = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
class email_check(FlaskForm):
    email = EmailField('Name', validators=[InputRequired(), Email()])
class add_user(FlaskForm):
    email = EmailField('Active Email Address', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired()])

# for manage_products
class select_catalog(FlaskForm):
    catalogname = QuerySelectField(query_factory=product_catalog, allow_blank=False)
class catalog_forms(FlaskForm):
    catalog = StringField('New Catalog', validators=[InputRequired()])
class add_products(FlaskForm):
    categories = QuerySelectField('Product Category', query_factory=product_catalog, allow_blank=False)
    name = StringField('Product Name', validators=[InputRequired()])
    price = IntegerField('Product Price', validators=[InputRequired()])
    quantity = IntegerField('Product Quantity (if none leave blank)')
    
# for managing the customers
class customer(FlaskForm):
    name = StringField('Customer Name', validators=[InputRequired()])
    contact_number = IntegerField('Contact Number', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    markers = StringField('Markers o Palatandaan', validators=[InputRequired()])
class transaction(FlaskForm):
    customertype = SelectField('Customer Type', choices=[
        ('regular', 'Regular Customer'), ('guest', 'Guest Customer')])
    optioncustomer =  StringField ('Name of Guest Customer', validators=[InputRequired()])
    customername = QuerySelectField('Name of Customer',query_factory=customer_catalog, allow_blank=False)
    contact_number = IntegerField('Contact Number', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    markers = StringField('Markers o Palatandaan', validators=[InputRequired()])
class product_transaction(FlaskForm):
    categories = QuerySelectField('Product Category', query_factory=product_catalog, allow_blank=False)
    qty = IntegerField('Quantity', validators=[InputRequired()])

class silent_form(FlaskForm):
    """
    Silent adding of users in database used for,
    manual migrations
    """
    email = EmailField('Email', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    hash_pw = StringField('Hashed Password (Optional)', validators=[InputRequired()])
    user_roles = SelectField('User Role', choices=[
        ('Admin', 'Admin'), ('Staff', 'Staff')
    ])