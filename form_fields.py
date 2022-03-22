from flask import Flask
from api.helpers import product_catalog
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, EmailField, SelectField, IntegerField
from wtforms.validators import InputRequired, Email
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
class email_check(FlaskForm):
    email = EmailField('Name', validators=[InputRequired(), Email()])
class add_user(FlaskForm):
    email = EmailField('Active Email Address', validators=[InputRequired(), Email()])
    username = StringField('Username', validators=[InputRequired()])

# for manage_products
class select_catalog(FlaskForm):
    categories = QuerySelectField(query_factory=product_catalog, allow_blank=False)
class catalog_forms(FlaskForm):
    catalog = StringField('New Catalog', validators=[InputRequired()])
class add_products(FlaskForm):
    categories = QuerySelectField('Product Name', query_factory=product_catalog, allow_blank=False)
    name = StringField('Product Name', validators=[InputRequired()])
    quantity = IntegerField('Product Quantity (if none leave blank)')