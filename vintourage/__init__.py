import os
import sentry_sdk
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sentry_sdk.integrations.flask import FlaskIntegration

from .config import Config


DEBUG = os.environ.get("FLASK_DEBUG", default=False)
if not DEBUG:
    sentry_sdk.init(
        dsn="https://4af5bb6641d04d888a3d762bd20bdf14@sentry.io/1472720",
        integrations=[FlaskIntegration()]
    )

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import context_processors, routes, models