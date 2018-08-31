# -*- coding: utf-8 -*-
import scrapy

def clean_whitespaces(value):
    if not value:
        return
    return value.replace('\n','').replace('\t','').replace(' ', '')


class SomavintageSpider(scrapy.Spider):
    name = 'somavintage'
    allowed_domains = ['somavintagestore.com']
    start_urls = ['http://somavintagestore.com/ubrania/sukienki']

    def get_price_for_product(self, product):
        """Get the price of the product.

        Normally a price will be visible inside div.price, but if there's
        a sale we should take the value from span.price-new.
        """
        selectors = [
            'div.product-meta div.price span.price-new::text',
            'div.product-meta div.price::text'
        ]
        for selector in selectors:
            price = product.css(selector).extract_first()
            price = clean_whitespaces(price)
            if price:
                return price

    def parse(self, response):
        for product in response.css('div.products-block div.product-block'):

            name = product.css('div.product-meta h3.name a::text').extract_first()
            if "KIDS" in name:
                continue

            yield {
                'name': name[:49],
                'image': product.css('div.image a.img-back img::attr(src)').extract_first(),
                'price': self.get_price_for_product(product),
                'link': product.css('div.image a.img-back::attr(href)').extract_first()
            }

        # Pagination next page is always after a bold element
        next_page = response.css('div.pagination .links b + a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
