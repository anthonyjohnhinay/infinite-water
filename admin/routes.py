

from flask import Blueprint, render_template
from form_fields import *
from db.models import Admin, Catalog
from db.database import db
from flask_login import current_user, login_required
admin = Blueprint('admin', __name__,
static_folder='static', template_folder='templates', static_url_path='/static/admin')

#registering the api blueprint
from api.routes import api
admin.register_blueprint(api, url_prefix='/api')

@admin.route('/')
def index():
    return render_template('dashboard.html')
@admin.route('/users')
def users():
    users_all =  db.session.query(Admin).order_by(Admin.id.desc()).limit(10).all()
    print(users_all)
    return render_template('manage_user.html', users=users_all)
#add users 
@admin.route('/users/add')
def add_users():
    form = add_user()
    return render_template('add_users.html', form=form)

#edit users
@admin.route('users/edit/<id>')
def edit_users(id):
    name = Admin.query.filter_by(id=id).first()
    form = add_user()
    return render_template('admin_edit.html', form=form, name=name)

@admin.route('/products')
def manage_product():
    form1 = select_catalog()
    form2 = catalog_forms()
    form3 = add_products()
    product_catalog = db.session.query(Catalog).order_by(Catalog.id.desc()).all()
    return render_template('manage_products.html', form1=form1, form2=form2, form3=form3,
    catalog=product_catalog)
