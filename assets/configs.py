
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
class betaconfig(Config):
    """
    Beta Database for unreleased version, use this to avoid
    f*cked up DB on production
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://zbcolxmj:uHEl_ZeICEWl5EDlCql5YSBat8wQ3cEt@satao.db.elephantsql.com/zbcolxmj'
class prodconfig(Config):
    """
    Use this class when hosting online or production mode
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://zhhvbyzcbrygqp:8ced37f5449d5fcb12eb2651c4a269d84a2ab7a5c1f548977f668a85180b4693@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d7nmvln4ji7uo4'
class prod2_config(Config):
    """
    Second migration for the DB (permanent)
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://htzpcdciorgdfb:a7687fc6eacb82a26c773c2711a012f7f131c7ddc7f596f0c6534debc72234f2@ec2-34-194-158-176.compute-1.amazonaws.com:5432/d5ufep761otd0f'