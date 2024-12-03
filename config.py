from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,".env"))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')
    UPLOAD_FOLDER_VIDEO = environ.get('UPLOAD_FOLDER_VIDEO')
    ADMIN_U = environ.get('ADMIN_U')
    ADMIN_P = environ.get('ADMIN_P')


class ProdConfig(Config):
    """Production config."""
    FLASK_ENV = "production"
    FLASK_DEBUG = False


class DevConfig(Config):
    """Development config."""
    FLASK_ENV = "development"
    FLASK_DEBUG = True