# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from .. import db
from ..models import Product

logger = logging.getLogger(__name__)


class ValidationPipeline(object):
    pass


class DatabasePipeline(object):
    def process_item(self, product_dict, spider):
        product = Product.query.filter_by(link=product_dict['link']).first()
        if not product:
            product = Product(**product_dict)
            db.session.add(product)
        else:
            product.update(**product_dict)

        db.session.commit()
