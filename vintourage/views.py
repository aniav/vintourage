from flask import render_template
from sqlalchemy import desc

from .database import db_session
from .models import Product
from . import app


@app.route('/')
def hello_world():
    products = Product.query.order_by(desc(Product.created))
    return render_template('index.html', products=products)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()