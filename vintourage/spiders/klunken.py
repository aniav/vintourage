# -*- coding: utf-8 -*-
import scrapy


class KlunkenSpider(scrapy.Spider):
    name = 'klunken'
    allowed_domains = ['klunken.pl']
    start_urls = ['http://klunken.pl/kategoria-produktu/kobieta/sukienki/']

    def parse(self, response):
        for product in response.css('li.product'):
            if product.css('a.product_type_simple::text').extract_first() == 'Sprzedany':
                continue

            yield {
                'name': product.css('h2.woocommerce-loop-product__title::text').extract_first(),
                'image': product.css('img::attr(src)').extract_first(),
                'price': product.css('span.woocommerce-Price-amount::text').extract_first(),
                'link': product.css('a.woocommerce-LoopProduct-link::attr(href)').extract_first()
            }

        next_page = response.css('li a.next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)