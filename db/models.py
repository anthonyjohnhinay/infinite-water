
from sqlalchemy.orm import backref
from db.database import db
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime

# user admin manage
class Admin(db.Model, UserMixin):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    user = db.Column(db.String(50), unique=True)
    #since it is hashed it has many characters
    password = db.Column(db.String(255))
    
  
#for products and catalog one to many
class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    # using cascade it will delete the parent together with its child.
    products = db.relationship('Product', backref=backref('catalog', uselist=False))
    def __repr__(self):
        return f'{self.name}'
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'))

# this is used to avoid any errors when browsing not login
class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Guest'