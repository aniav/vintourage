import datetime
from collections import defaultdict
from flask import render_template
from sqlalchemy import desc

from . import app
from .models import Product


@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>')
def index(page=1):
    products = (
        Product.query
        .order_by(desc(Product.created))
        .paginate(page, app.config['PAGINATION_PAGE_SIZE'], error_out=False)
    )

    products_by_date = defaultdict(list)
    for product in products.items:
        create_date = product.created.date()
        products_by_date[create_date].append(product)

    context = {
        "products": products,
        "products_by_date": products_by_date
    }
    return render_template('index.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')