import scrapy
from scrapy.crawler import CrawlerProcess

from .dewitched import DewitchedSpider
from .klunken import KlunkenSpider
from .ragsandsilks import RagsandsilksSpider
from .somavintage import SomavintageSpider
from .vintageladies import VintageladiesSpider

process = CrawlerProcess()
process.crawl(DewitchedSpider)
process.crawl(KlunkenSpider)
process.crawl(RagsandsilksSpider)
process.crawl(SomavintageSpider)
process.crawl(VintageladiesSpider)
process.start() # the script will block here until all crawling jobs are finished