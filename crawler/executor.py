import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .spiders.dewitched import DewitchedSpider
from .spiders.inspired import InspiredSpider
from .spiders.klunken import KlunkenSpider
from .spiders.ragsandsilks import RagsandsilksSpider
from .spiders.somavintage import SomavintageSpider
from .spiders.vintageladies import VintageladiesSpider

from .constants import Categories


from vintourage import app, db


crawlers = [
    DewitchedSpider,
    #InspiredSpider, KlunkenSpider, RagsandsilksSpider,
    #SomavintageSpider, VintageladiesSpider
]

process = CrawlerProcess(get_project_settings())

for crawler_class in crawlers:
    print(f'Processing crawler {crawler_class.name}')

    for category in crawler_class.category_mapping.keys():
        print(f'Attempting to crawl {category.name}')
        print(f'{category.value}')
        crawler = crawler_class(category=category)

        process.crawl(crawler)

process.start() # the script will block here until all crawling jobs are finished