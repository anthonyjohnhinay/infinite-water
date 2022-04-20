
from flask import Blueprint
from db.database import db
from db.models import *
from datetime import datetime
api_graph = Blueprint('api_graph', __name__)
"""
This module is used for getting the graphs e.g the latest count of sales or total sales
"""
@api_graph.route('/')
def index():
    return 'Welcome to Graphs API'
@api_graph.route('/today')
def get_today():

    return '200'