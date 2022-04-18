
from flask import Blueprint, jsonify, request, render_template
from api.helpers import time
from assets.form_fields import transaction

from db.models import *
from db.database import db

api_transaction= Blueprint('api_transaction', __name__)

@api_transaction.post('/delete')
def transaction_delete():
    trans_id = request.form['id']
    data = transaction_data.query.filter_by(id=trans_id).delete()
    try:
        db.session.commit()
    finally:
        db.session.close()
    return jsonify({'success' : 'deleted the transaction'})
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
@api_transaction.post('/fetch_transaction')
def get_transaction():
        customername = request.form['customername']
        customercontact = request.form['customercontact']
        customeraddress =  request.form['customeraddress']
        deliverystatus = request.form['deliverystatus']
        productcatalog = request.form['productcatalog']
        productname = request.form['productname']
        productprice = request.form['productprice']
        producttotal = request.form['producttotal']
        userbal = request.form['userbal']
        qty = request.form['qty']
        print(customername, productname, qty)
        add_customer = transaction_data(customername = customername.title(),
        customercontact = customercontact,
        productstatus = deliverystatus,
        customeraddress = customeraddress,
        productcatalog = productcatalog,
        productname = productname,
        total = producttotal,
        qty = qty,
        productprice = productprice,
        productbal = userbal
        )
        db.session.add(add_customer)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)})
        finally:
            db.session.close()
        return '200'
# fetch in edit status of client product
@api_transaction.post('/edit')

def fetch_status():
    tid = request.form['id']
    if 'newstatus' in request.form:
        status = request.form['newstatus']
        update = transaction_data.query.filter_by(id=tid).update(dict(productstatus=status, transac_stat=time()))
        try:
            db.session.commit()
        finally:
            db.session.close()
    
    transaction = transaction_data.query.filter_by(id=tid).first()
    return jsonify({
        'status' : transaction.productstatus,
        'time' : transaction.transac_stat

    })

@api_transaction.post('/editall')
def fetch_all():
    tid = request.form['id']
    transaction = transaction_data.query.filter_by(id=tid).first()
    return jsonify({
        'customername' : transaction.customername,
        'customercontact' : transaction.customercontact,
        'customeraddress' : transaction.customeraddress,
        'productstatus' : transaction.productstatus,
        'productcatalog' : transaction.productcatalog,
        'productname' : transaction.productname,
        'total' : transaction.total,
        'qty' : transaction.qty,
        'productprice' : transaction.productprice,
        'productbal' : transaction.productbal,

    })
@api_transaction.post('/editsubmit')
def editsubmit():
        id= request.form['id']
        customername = request.form['customername']
        customercontact = request.form['customercontact']
        customeraddress =  request.form['customeraddress']
        deliverystatus = request.form['deliverystatus']
        productcatalog = request.form['productcatalog']
        productname = request.form['productname']
        productprice = request.form['productprice']
        productprice = int(productprice)
        producttotal = request.form['producttotal']
        producttotal = int(producttotal)
        userbal = request.form['userbal']
        userbal = int(userbal)
        qty = request.form['qty']
        print(customername, productname, qty)
        add_customer = transaction_data.query.filter_by(id=id).update(dict(
        customername = customername.title(),
        payment_stat = time(),
        customercontact = customercontact,
        productstatus = deliverystatus,
        customeraddress = customeraddress,
        productcatalog = productcatalog,
        productname = productname,
        total = producttotal,
        qty = qty,
        productprice = productprice,
        productbal = userbal
        ))
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)})
        finally:
            db.session.close()
        return '200'
            
            
            
            
            
            
           