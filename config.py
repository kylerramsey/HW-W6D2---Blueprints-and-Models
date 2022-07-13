import os
from dotenv import load_dotenv

# Getting the path to the current project
basedir = os.path.abspath(os.path.dirname(__name__)) 

# Taking the path, and finding the absolute path to our .env file
# and loading the variables into our environment
# basedir + '\\' + '.env'
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    # FLASK_APP = 'development'
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')