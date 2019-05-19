import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .dewitched import DewitchedSpider
from .klunken import KlunkenSpider
from .ragsandsilks import RagsandsilksSpider
from .somavintage import SomavintageSpider
from .vintageladies import VintageladiesSpider

crawlers = [
    DewitchedSpider,
    KlunkenSpider, RagsandsilksSpider, SomavintageSpider,
    VintageladiesSpider
]
process = CrawlerProcess(get_project_settings())
for crawler in crawlers:
    process.crawl(crawler)

process.start() # the script will block here until all crawling jobs are finished