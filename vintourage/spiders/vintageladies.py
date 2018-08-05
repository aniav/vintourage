# -*- coding: utf-8 -*-
import scrapy


class VintageladiesSpider(scrapy.Spider):
    name = 'vintageladies'
    allowed_domains = ['vintageladies.pl']
    start_urls = ['http://vintageladies.pl/']

    def parse(self, response):
        pass
