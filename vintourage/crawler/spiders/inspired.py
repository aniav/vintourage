# -*- coding: utf-8 -*-
import tinycss2

from crawler.base import CategorySpider


class InspiredSpider(CategorySpider):
    name = 'inspired'
    allowed_domains = ['inspired.sklep.pl']
    category_mapping = {
        Categories.sukienki: ['https://inspired.sklep.pl/kategoria-produktu/sukienki/']
    }

    def parse(self, response):
        for product in response.css('li.htheme_single_wc_item'):
            background_img_style = product.css('div.htheme_inner_col::attr(style)').get()
            # get product image from style="background-image:url(...)"
            image = tinycss2.parse_declaration_list(background_img_style)[0].value[0].value
            tooltip_text = product.css('a.htheme_icon_list_product_add::attr(data-tooltip-text)').get()

            # if tooltip text doesn't say we can add to cart we assume the product is inactive
            active = 'Dodaj do' in tooltip_text

            yield {
                'name': product.css('a.htheme_product_list_title::text').get(),
                'image': image,
                'price': product.css('div.htheme_product_list_price span::text').get(),
                'link': product.css('a.htheme_product_item_link::attr(href)').get(),
                'active': active
            }

        next_page = response.css('nav a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
