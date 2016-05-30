# import scrapy
# from scrapy.contrib.spiders import CrawlSpider, Rule
# # from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
# from scrapy.selector import HtmlXPathSelector
# from scrapy.linkextractors import LinkExtractor


# class gsm_spyder(scrapy.Spider):
#     name = "gsmarena"
#     allowed_domains = ["www.gsmarena.com"]
#     start_urls = [
#         "http://www.gsmarena.com/",
#         "http://www.gsmarena.com/product-category/living-room/display-units/"
#     ]

#     rules = (
#         Rule(LinkExtractor(allow=('http://www.gsmarena.com/', ),), callback='parse', follow=False),
#         Rule(LinkExtractor(allow=('http://www.gsmarena.com/', ),), follow=True),
#         )

#     def parse(self, response):
#         filename = response.url.split("/")[-2] + '.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
# -*- coding: utf-8 -*-


import time
import re
import scrapy
import time
# from skoov_parser.parsers import parse_biba
from pprint import pprint
from content_parser import content_parser
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from base_spider import SkoovSpider
from lxml import html
import requests

class gsm_spyder(CrawlSpider):
    name = "gsmarena"
    rules = (
        Rule(LinkExtractor(allow=('http://www.gsmarena.com/', ),), callback='parse_custom', follow=True),
        # Rule(LinkExtractor(allow=('http://www.gsmarena.com/', ),), follow=True),
        )

    #custom_settings = {"SKOOV_HTTP_ENABLED": True, "SKOOV_HTTP_PROXY": "http://45.33.106.64:8123"}
    
    def __init__(self):
        self.domain = "www.gsmarena.com"
        self.name = "gsmarena"
        self.custom_settings = {}
        self.allowed_domains = ["www.gsmarena.com"]
        CrawlSpider.__init__(self)
        self.start_urls = ["http://www.gsmarena.com/","http://www.gsmarena.com/makers.php3"]
        self.count = 0
        self.deny = ""
        self.crawl_limt = 0
        self.real_count = 0

    def parse_custom(self, response):
        """ Parse the response """

        #self.parse(response)
        content = response.body
        self.logger.info('Parse function called on %s', response.url)
        product_url = content_parser(content,response.url)
        print "######## URL IS==> ",product_url
        # Parse the content
        # product_json = parse_biba.parse(content, response.url)
        # pprint(product_json)
        # self.r.incr(self.name + "_total_count")
        # if len(product_json) > 0:
            # self.r.incr(self.name + "_real_count")
            # self.real_count += 1
        # self.write_json_to_cache(product_json)
        # TBD - Ingest the JSON or write it to DB
        # print response.url
        self.count += 1
        print "Count =>",self.count
        if self.real_count > self.crawl_limt:
            raise CloseSpider('crawl limit ==>>done')