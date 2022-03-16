from db.database import db
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime

# user admin manage
class Admin(db.Model, UserMixin):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

# this is used to avoid any errors when browsing not login
class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.username = 'Guest'