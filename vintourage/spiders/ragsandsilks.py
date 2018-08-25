# -*- coding: utf-8 -*-
import scrapy


class RagsandsilksSpider(scrapy.Spider):
    name = 'ragsandsilks'
    allowed_domains = ['ragsandsilks.pl']
    start_urls = ['https://ragsandsilks.pl/pl/c/SUKIENKI/20']

    def parse(self, response):
        for product in response.css('div.product'):
            image_uri = product.css('a.prodimage img::attr(src)').extract()[1]
            product_uri = product.css('a.prodname::attr(href)').extract_first()

            yield {
                'name': product.css('span.productname::text').extract_first(),
                'image': response.urljoin(image_uri),
                'price': product.css('div.price em::text').extract_first(),
                'link': response.urljoin(product_uri)
            }

        next_page = response.css('ul.paginator li.last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

