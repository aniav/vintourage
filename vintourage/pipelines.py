# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from . import db
from .models import Product

logger = logging.getLogger(__name__)


class ValidationPipeline(object):
    pass


class DatabasePipeline(object):
    def process_item(self, item, spider):
        if Product.query.filter(Product.link==item['link']).scalar() is not None:
            logger.info('Product with link %s already exists', item['link'])
            return

        product = Product(**item)
        db.session.add(product)
        db.session.commit()
