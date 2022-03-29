from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from config import *
from db.models import Admin, Anonymous
from db.database import db
from os import path
"""
Declaring all the necessary dependecies needed for
the project.   
"""
def config_app():
    app = Flask(__name__)
    # this is for debug purposes always set to TRUE in config_prod to get any problems when developing.
    app.config['DEBUG'] = config_prod
    app.config['SECRET_KEY'] = config_secret
    app.config['SQLALCHEMY_DATABASE_URI'] = config_db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config_track_modifications
      
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'login.index'
    login_manager.anonymous_user = Anonymous
    login_manager.init_app(app)
    bootstrap = Bootstrap4(app)
    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))
    
    # for registering the blueprints in the main function
    from admin.routes import admin
    app.register_blueprint(admin, url_prefix='/admin')
    from login.routes import login
    app.register_blueprint(login, url_prefix='/')
    from errors.routes import error
    app.register_blueprint(error)


    return app
# this is used for registering db models into sql
def setup_database(app):
    with app.app_context():
        db.create_all()   
# setting up the default admin, this can be setup in the config.py
def make_admin(app):
    with app.app_context():
        email = config_email
        pw = generate_password_hash(config_password, 'sha256')
        create_user = Admin(email=email, password=pw)
        db.session.add(create_user)
        try:
            print('executed')
            db.session.commit()
        except Exception as e:
            pass
            #print(e) # this is implemented to detect any errors instead of using pass which to silent any errors



if __name__ == '__main__':
    app = config_app()
    if not path.isfile('/db/admin.db'):
        setup_database(app)
        make_admin(app)
    
    app.run(host=config_host)
