import re
from flask import Blueprint, jsonify, redirect, render_template, url_for, flash, request
from db.models import *
from db.database import *
from form_fields import *
""""
This branch route in the api is used only for the customers
"""
api_customer = Blueprint('api_customer', __name__)

@api_customer.post('/edit/<id>')
def edit_customer(id):
    customer_name = request.form['customers']
    address = request.form['address']
    contact = request.form['contact']
    markers = request.form['markers']
    if address == '':
        address = None
    if contact == '':
        contact = None
    if markers == '':
        markers = None
    edit_customers = Customer.query.filter_by(id=id).update(dict(
        name=customer_name,
        contact_number = contact,
        address = address,
        markers = markers
    ))
    db.session.commit()
    return '200'
@api_customer.get('/delete/<id>')
def delete_customer(id):
    del_customer = Customer.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Succesfully delete the customer', 'success')
    return redirect(url_for('admin.manage_customers'))

@api_customer.post('/add')
def add_customer():
    customer = request.form['customer']
    address = request.form['address']
    contact_num = request.form['contact_num']
    marker = request.form['marker']
    if address == '':
        address = None
    if contact_num == '':
        contact_num = None
    if marker == '':
        marker = None
    print(customer)
    new_customer = Customer(
        name=customer.title(),
        contact_number = contact_num,
        address = address,
        markers = marker
    )
    db.session.add(new_customer)
    try:
        db.session.commit()
    except:
        return jsonify({'error': 'Customer already exist!'})
    return jsonify({'success': 'Succefully added the customer'})
