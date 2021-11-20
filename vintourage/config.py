import os
basedir = os.path.abspath(os.path.dirname(__file__))

fallback_db = 'sqlite:///' + os.path.join(basedir, 'simple.db')

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', fallback_db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGINATION_PAGE_SIZE = 39