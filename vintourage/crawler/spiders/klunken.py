# -*- coding: utf-8 -*-
from crawler.base import CategorySpider


class KlunkenSpider(CategorySpider):
    name = 'klunken'
    allowed_domains = ['klunken.pl']
    category_mapping = {
        Categories.sukienki: ['http://klunken.pl/kategoria-produktu/kobieta/sukienki/']
    }

    def parse(self, response):
        for product in response.css('li.product'):
            active = product.css('a.product_type_simple::text').get() != 'Sprzedany'

            yield {
                'name': product.css('h2.woocommerce-loop-product__title::text').get(),
                'image': product.css('img::attr(src)').get(),
                'price': product.css('span.woocommerce-Price-amount::text').get(),
                'link': product.css('a.woocommerce-LoopProduct-link::attr(href)').get(),
                'active': active
            }

        next_page = response.css('li a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)