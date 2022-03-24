from logging import exception
import re
from flask import Blueprint, jsonify, redirect, render_template, url_for, flash, request
from db.models import *
from db.database import *
from form_fields import *
""""
This branch route in the api is used only for the product catalogs
"""
api_product = Blueprint('api_product', __name__)

#for products and categories
@api_product.route('/products/<id>')
def catalog_delete_post(id):
    category = Catalog.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Succesfully deleted the catalog name', 'success')
    return redirect(url_for('admin.manage_product'))
@api_product.post('/catalogs')
def catalog():
    data = request.form['catalogs']
    data=data.title()
    product_catalog = Catalog(name=data)
    db.session.add(product_catalog)
    try:
        db.session.commit()
    except:
        return jsonify({'error':f'{data} has been already in the product catalogs!'})
    return jsonify({'success':f'{data} has been added in product catalogs!'})
@api_product.post('/filter')
def filter_select():
    data = request.form['product']
    print(data)
    #getting the product data from the ajax request
    catalog = Catalog.query.filter_by(name=data).first()
    print(catalog.products.name)
    return '200'

#what is does is adding a product then if the quantity is None e.g a refill
@api_product.post('/add')
def add_product():
   selectprod = request.form['selectprod']
   productname = request.form['productname'].title()
   price = request.form['price']
   qty = request.form['qty']
   if qty == "":
       qty = None
   else:
       qty = int(qty)
   print(selectprod, productname, price, qty)
   catalog = Catalog.query.filter_by(name=selectprod).first()
   product = Product(name=productname, price=price, quantity=qty, catalog=catalog)
   db.session.add(product)
   try:
       db.session.commit()
   except Exception as e:
       print(e)

   return jsonify({'success': f'{productname} product has been added to catalog'})
   