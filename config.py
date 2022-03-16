# this can be replaced the var below with env for privacy purposes
from os import getenv



config_host = '0.0.0.0'
config_secret = 'secret_project'
config_prod = True

"""
This are the variables for the database,
you can use sqlite3 via sqlite:/// <directory>/<name of file>.db
or a postgres server via postgresql:///<user>:<password>@<url>/<db>
"""
config_db = 'sqlite:///db/admin.db'
config_track_modifications = False #set on False to remove any warnings during startup

"""
setting up the default username and password for
admin
"""
config_email = 'root@admin.org'
config_password = 'admin'