import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorageaccount'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-sql-server1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    # Adjust the driver version if necessary
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME
        + ':'
        + SQL_PASSWORD
        + '@'
        + SQL_SERVER
        + ':1433/'
        + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    AUTHORITY = 'https://login.microsoftonline.com/common'  # For multi-tenant app
    CLIENT_ID = os.environ.get('CLIENT_ID')
    REDIRECT_PATH = '/getAToken'  # Must match the redirect URI set in AAD

    SCOPE = ['User.Read']  # Only need to read the user profile
    SESSION_TYPE = 'filesystem'  # Token cache will be stored in server-side session
