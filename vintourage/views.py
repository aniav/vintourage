import datetime
from collections import defaultdict
from flask import render_template
from sqlalchemy import desc

from .database import db_session
from .models import Product
from . import app


@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    three_days_ago = datetime.datetime.now().date() - datetime.timedelta(days=7 * page)

    products = (
        Product.query
        .filter(Product.created >= three_days_ago)
        .order_by(desc(Product.created))
        .limit(50)
    )

    products_by_date = defaultdict(list)
    for product in products:
        create_date = product.created.date()
        products_by_date[create_date].append(product)

    return render_template('index.html', products_by_date=products_by_date, page=page)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()