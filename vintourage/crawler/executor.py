import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.dewitched import DewitchedSpider
from spiders.inspired import InspiredSpider
from spiders.klunken import KlunkenSpider
from spiders.ragsandsilks import RagsandsilksSpider
from spiders.somavintage import SomavintageSpider
from spiders.vintageladies import VintageladiesSpider

crawlers = [
    DewitchedSpider, InspiredSpider, KlunkenSpider, RagsandsilksSpider,
    SomavintageSpider, VintageladiesSpider
]
process = CrawlerProcess(get_project_settings())
for crawler in crawlers:
    process.crawl(crawler)

process.start() # the script will block here until all crawling jobs are finished