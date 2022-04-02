
from flask import Blueprint, jsonify, request, render_template

from db.models import *
from db.database import db

api_transaction= Blueprint('api_transaction', __name__)

@api_transaction.post('/request')
def get_customer():
    customer = request.form['customer']
    customer = Customer.query.filter_by(name=customer).first()
    return jsonify({
        'contact' : customer.contact_number,
        'address' : customer.address,
        'markers' : customer.markers
    })
@api_transaction.post('/fetch_product')
def get_child_product():
    product = request.form['categories']
    product = Catalog.query.filter_by(name=product).first()
    catalog = product.products
    return jsonify({
        'response' : render_template('response/product.html', product=catalog)
    })