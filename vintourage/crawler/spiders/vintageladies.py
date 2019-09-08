# -*- coding: utf-8 -*-
from crawler.base import CategorySpider
from vintourage.constants import Categories


class VintageladiesSpider(CategorySpider):
    name = 'vintageladies'
    allowed_domains = ['vintageladies.pl']
    category_mapping = {
        Categories.bluzki_damskie: [
            'http://vintageladies.pl/index.php?cPath=21_22',
            'http://vintageladies.pl/index.php?cPath=21_23',
        ],
        Categories.sukienki: [
            'http://vintageladies.pl/index.php?cPath=31_33',
            'http://vintageladies.pl/index.php?cPath=31_34',
        ],
        Categories.swetry_damskie: [
            'http://vintageladies.pl/index.php?cPath=24',
        ],
        Categories.spodnice: [
            'http://vintageladies.pl/index.php?cPath=25_26',
            'http://vintageladies.pl/index.php?cPath=25_27',
            'http://vintageladies.pl/index.php?cPath=25_28',
            'http://vintageladies.pl/index.php?cPath=25_29',
        ]
    }

    def parse(self, response):
        for product in response.xpath('//td[@valign = "top" and @width = "169"]'):
            active = 'SPRZEDAN' not in product.xpath('.//td[@class = "fe2"]/a/text()').get()

            image_uri = product.xpath('.//td[@class = "bg"]//img/@src').get()

            # Rmove the osCsid argument as it breaks links
            link = product.xpath('.//td[@class = "bg"]//a/@href').get()
            parts = [part for part in link.split("&") if "osCsid" not in part]
            link = "&".join(parts)

            yield {
                'name': product.xpath('.//td[@class = "fe2"]/a/text()').get()[:49],
                'image': response.urljoin(image_uri),
                'price': product.xpath('.//td[@class = "fe1"]/span/text()').get(),
                'link': link,
                'active': active,
            }

        selector = '//a[@class = "pageResults" and contains(@title, "Następna")]/@href'
        next_page = response.xpath(selector).get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
