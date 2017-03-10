import os
from mosaic.controller.Image2Mosaic import fill_color_map


class Config:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    SECRET_KEY = 'f77afd1f2e306abfeb0c6aede2fdf6b5'

    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    FRAGMENT_SHAPE = 60
    FRAGMENTS_DIR = os.path.join(BASEDIR, 'img')
    COLOR_MAP = fill_color_map(FRAGMENTS_DIR)

    UPLOADED_PHOTOS_DEST = os.path.join(BASEDIR, 'tmp')
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


class DevelopConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
