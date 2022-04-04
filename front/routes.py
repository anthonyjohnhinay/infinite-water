from flask import Blueprint, render_template

front = Blueprint('front', __name__,
static_folder='static', template_folder='templates', static_url_path='/static/front')

@front.route('/')
def index():
    return render_template('home.html', title='Infinity Flow')