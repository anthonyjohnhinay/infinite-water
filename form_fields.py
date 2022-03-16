from flask import Flask

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, EmailField, SelectField
from wtforms.validators import InputRequired, Email
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
    role = SelectField('Roles', choices=[('Admin', 'Admin'), ('Staff', 'Staff')], validators=[InputRequired()] )