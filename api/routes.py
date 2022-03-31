
from flask import Blueprint

"""
This route is only used for the interaction between the database and the users (POST) request
"""
api = Blueprint('api', __name__)

"""
We nested the routes to minimize the contents and organize all
"""
from .branch.products import api_product
api.register_blueprint(api_product, url_prefix='/products')

from .branch.users import api_users
api.register_blueprint(api_users, url_prefix="/users")

from .branch.customers import api_customer
api.register_blueprint(api_customer, url_prefix='/customers')