# -*- coding: utf-8 -*-
import scrapy
import tinycss2


class InspiredSpider(scrapy.Spider):
    name = 'inspired'
    allowed_domains = ['inspired.sklep.pl']
    start_urls = ['https://inspired.sklep.pl/kategoria-produktu/sukienki/']

    def parse(self, response):
        for product in response.css('li.htheme_single_wc_item'):
            background_img_style = product.css('div.htheme_inner_col::attr(style)').extract_first()
            # get product image from style="background-image:url(...)"
            image = tinycss2.parse_declaration_list(background_img_style)[0].value[0].value

            yield {
                'name': product.css('a.htheme_product_list_title::text').extract_first(),
                'image': image,
                'price': product.css('div.htheme_product_list_price span::text').extract_first(),
                'link': product.css('a.htheme_product_item_link::attr(href)').extract_first()
            }

        next_page = response.css('nav a.next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
