# -*- coding: utf-8 -*-
import scrapy


class DewitchedSpider(scrapy.Spider):
    name = 'dewitched'
    allowed_domains = ['www.dewitched.pl']
    start_urls = ['https://www.dewitched.pl/dla-pan-cat-5']

    def parse(self, response):
        main_list = response.css('div.products-list')[0]
        for product in main_list.css('div.product'):
            image_uri = product.css('figure.product-image img::attr(src)').extract_first().lstrip('.')

            yield {
                'name': product.css('strong.product-name::text').extract_first(),
                'image': response.urljoin(image_uri),
                'price': product.css('span.product-price strong::text').extract_first(),
                'link': product.css('a.product-area::attr(href)').extract_first()
            }
