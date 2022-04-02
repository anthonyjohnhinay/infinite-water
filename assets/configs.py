
"""
setting up the default username and password for
admin
"""
config_email = 'root@admin.org'
config_password = 'admin'
config_username = 'root'


class Config:
    """ Base configurations between the prod and test server """
    SECRET_KEY = 'secret_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email services
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME = 'infinityflow.inventory@gmail.com'
    MAIL_PASSWORD = 'Infinityflow0402'

class testconfig(Config):
    """
    For TESTING purposes only
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/admin.db'
    SERVER_NAME = '100.115.92.197:5000'
class prodconfig(Config):
    """
    Use this class when hosting online or production mode
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres server'
    SERVER_NAME = '100.115.92.197:5000'