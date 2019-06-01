# -*- coding: utf-8 -*-
import scrapy


class RagsandsilksSpider(scrapy.Spider):
    name = 'ragsandsilks'
    allowed_domains = ['ragsandsilks.pl']
    start_urls = ['https://ragsandsilks.pl/pl/c/SUKIENKI/20']

    def parse(self, response):
        for product in response.css('div.product'):
            image_uri = product.css('a.prodimage img::attr(src)').getall()[1]
            product_uri = product.css('a.prodname::attr(href)').get()

            # if the basket button is not there we assume the product is inactive
            actvie = bool(product.css('a.addtobasket').get())

            yield {
                'name': product.css('span.productname::text').get(),
                'image': response.urljoin(image_uri),
                'price': product.css('div.price em::text').get(),
                'link': response.urljoin(product_uri),
                'active': actvie
            }

        next_page = response.css('ul.paginator li.last a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

