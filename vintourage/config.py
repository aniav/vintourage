import os
basedir = os.path.abspath(os.path.dirname(__file__))

fallback_db = 'sqlite:///' + os.path.join(basedir, 'simple.db')

uri = os.environ.get('DATABASE_URL', fallback_db)
# SQLAlchemy 1.4 removed the deprecated postgres dialect name
# but Heroku still uses that so we have to workaround it
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

class Config:
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGINATION_PAGE_SIZE = 39