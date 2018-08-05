# -*- coding: utf-8 -*-
import scrapy


class BreslauerinSpider(scrapy.Spider):
    name = 'breslauerin'
    allowed_domains = ['breslauerin.pl']
    start_urls = ['https://www.breslauerin.pl/sklep']

    def parse(self, response):
        self.log('Response %s' % response)
        for product in response.css('[product-item]'):
            self.log('Product %s' % product)
            if product.css('span.out-of-stock').extract_first() is not None:
                continue

            name = product.css('h3.title::text').extract_first()
            self.log('Name %s' % name)
            yield {
                'name': name,
                'image': product.css('img::attr(src)').extract_first(),
                'price': product.css('span.price span::text').extract_first(),
            }
