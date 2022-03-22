
from flask import Blueprint, render_template
error = Blueprint('error', __name__,
static_folder='static', template_folder='templates', static_url_path='/static/error')

"""
These are the error page for the website 
"""
@error.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404

@error.app_errorhandler(405)
def handle_405(err):
    return render_template('405.html'), 405
