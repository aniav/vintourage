# -*- coding: utf-8 -*-
import scrapy


class VintageladiesSpider(scrapy.Spider):
    name = 'vintageladies'
    allowed_domains = ['vintageladies.pl']
    start_urls = [
        'http://vintageladies.pl/index.php?cPath=31_32', # sukienki codzienne
        'http://vintageladies.pl/index.php?cPath=31_33', # sukienki koktajlowe
        'http://vintageladies.pl/index.php?cPath=31_34', # na wielki bal
    ]

    def parse(self, response):
        for product in response.xpath('//td[@valign = "top" and @width = "169"]'):

            if 'SPRZEDAN' in product.xpath('.//td[@class = "fe2"]/a/text()').extract_first():
                continue

            image_uri = product.xpath('.//td[@class = "bg"]//img/@src').extract_first()

            # Rmove the osCsid argument as it breaks links
            link = product.xpath('.//td[@class = "bg"]//a/@href').extract_first()
            parts = [part for part in link.split("&") if "osCsid" not in part]
            link = "&".join(parts)

            yield {
                'name': product.xpath('.//td[@class = "fe2"]/a/text()').extract_first()[:49],
                'image': response.urljoin(image_uri),
                'price': product.xpath('.//td[@class = "fe1"]/span/text()').extract_first(),
                'link': link,
            }

        selector = '//a[@class = "pageResults" and contains(@title, "Następna")]/@href'
        next_page = response.xpath(selector).extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
