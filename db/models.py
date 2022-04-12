
from sqlalchemy.orm import backref
from db.database import db
from db.models import *
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#from app import app
from datetime import datetime

# user admin manage
class Admin(db.Model, UserMixin):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    user = db.Column(db.String(50), unique=True)
    #since it is hashed it has many characters
    password = db.Column(db.String(255))

    def get_token(self, expire_sec = 1800):
        serial = Serializer(
            'secret',
            expire_sec
        )
        print(self.id)
        return serial.dumps({'user_id' : self.id})
    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer('secret')
    #     try:
    #         user_id = s.loads(token)['user_id']
    #         print(user_id)
    #     except:
    #         print('failed')
    #         return None
    #     return Admin.query.get(user_id)


# for customers
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    contact_number = db.Column(db.String(100))
    address = db.Column(db.String(255))
    markers = db.Column(db.String(255))
    def __repr__(self):
        return f'{self.name}'

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
class transaction_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transactionid = db.Column(db.Integer, unique=True)
    customername = db.Column(db.String(100))
    customercontact = db.Column(db.String(255))
    customeraddress = db.Column(db.String(255))
    customermarkers = db.Column(db.String(255))
    productcatalog = db.Column(db.String(100))
    productname = db.Column(db.String(100))
    total = db.Column(db.Integer)
    qty = db.Column(db.Integer)
    productprice = db.Column(db.Integer)
    productbal = db.Column(db.Integer)
    
# this is used to avoid any errors when browsing not login
class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.user = 'Guest'