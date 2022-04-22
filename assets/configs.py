
"""
setting up the default username and password for
admin
"""
config_email = ''
config_password = ''
config_username = ''


class Config:
    """ Base configurations between the prod and test server """
    SECRET_KEY = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email services
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

class testconfig(Config):
    """
    For TESTING purposes only
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/admin.db'
    SERVER_NAME = '100.115.92.197:5000'
class betaconfig(Config):
    """
    Beta Database for unreleased version, use this to avoid
    f*cked up DB on production
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'
class prodconfig(Config):
    """
    Use this class when hosting online or production mode
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'
class prod2_config(Config):
    """
    Second migration for the DB (permanent)
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://'