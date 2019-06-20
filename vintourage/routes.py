import datetime
from collections import defaultdict
from flask import render_template
from sqlalchemy import desc

from . import app
from .models import Product


@app.route('/')
def index():
    latest_products = (
        Product.query
        .filter_by(active=True)
        .order_by(desc(Product.created))
        .limit(6)
    )
    context = {
        "latest_products": latest_products,
    }
    return render_template('index.html', **context)


@app.route('/products')
@app.route('/products/page/<int:page>')
def products(page=1):
    products = (
        Product.query
        .filter_by(active=True)
        .order_by(desc(Product.created))
        .paginate(page, app.config['PAGINATION_PAGE_SIZE'], error_out=False)
    )
    context = {
        "products": products,
    }
    return render_template('shop.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')