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
    catalog = Product.query.filter_by(catalog_id=id).all()
    #krazy idea run instead in for loop =) 
    for product in catalog:
        Product.query.filter_by(catalog_id=id).delete()
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
    #form
    form1 = select_catalog()
    form2 = catalog_forms()
    form3 = add_products()

    data = request.form['product']
    print(data)
    #getting the product data from the ajax request
    product_catalog = db.session.query(Catalog).order_by(Catalog.id.desc()).all()
    catalog = Catalog.query.filter_by(name=data).first()
    catalog_child = catalog.products
    print(catalog_child)

    return render_template('manage_products.html', products=catalog_child,
    form1=form1, form2=form2, form3=form3, catalog=product_catalog )
@api_product.route('/delete/<id>')
def delete_content(id):
    data = Product.query.filter_by(id=id).delete()
    db.session.commit()
    flash('succesfully deleted the product', 'success')
    return redirect(url_for('admin.manage_product'))
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
   print(catalog)
   product = Product(name=productname, price=price, quantity=qty, catalog=catalog)
   db.session.add(product)
   try:
       db.session.commit()
   except:
       return jsonify({'error': f'{productname} is already exist'})
      
   return jsonify({'success': f'{productname} product has been added to catalog'})
   # product edits
@api_product.route('product/edit/<id>', methods=['GET', 'POST'])
def edit_prod(id):
    # post request
    category = request.form['category']
    productname = request.form['productname']
    price = request.form['price']
    qty = request.form['qty']
    catalog = Catalog.query.filter_by(name=category).first()
    print(catalog.id)
    update = Product.query.filter_by(id=id).update(dict(
        name = productname, price = price,
        quantity = qty, catalog_id = catalog.id
    ))
    db.session.commit()
    return '200'

@api_product.post('catalog/edit/<id>')
def edit_catalog(id):
    category = request.form['catalog']
    catalog = Catalog.query.filter_by(id=id).update(dict(name=category))
    db.session.commit()
    return '200'