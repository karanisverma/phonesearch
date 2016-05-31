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
from __future__ import print_function
import bleach
import re
import scrapy
import time
import json
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
        Rule(LinkExtractor(allow=('http://www.gsmarena.com/.+.php', ),
                           deny=('http://www.gsmarena.com/.*news.*',
                                 'http://www.gsmarena.com/.*switch.*',
                                 'http://www.gsmarena.com/.*reviewcomm.*',
                                 'http://www.gsmarena.com/.*postcomment.*',
                                 'http://www.gsmarena.com/.*compare.*',
                                 'http://www.gsmarena.com/.*glossary.*',
                                 'http://www.gsmarena.com/.*nickname.*',
                                 'http://www.gsmarena.com/.*facebook.*',
                                 'http://www.gsmarena.com/.*google.*',
                                 'http://www.gsmarena.com/.*whyregister.*',
                                 ' http://www.gsmarena.com/.*postopinion.*',
                                 'http://www.gsmarena.com/.*review.*')),
             callback='parse_custom', follow=True),)

        # Rule(LinkExtractor(allow=('http://www.gsmarena.com/', ),), follow=True),
             

    # custom_settings = {"HTTP_ENABLED": True, "HTTP_PROXY": "http://45.33.106.64:8123"}
    
    def __init__(self):
        self.domain = "www.gsmarena.com"
        self.name = "gsmarena"
        self.custom_settings = {}
        self.allowed_domains = ["www.gsmarena.com"]
        CrawlSpider.__init__(self)
        self.start_urls = ["http://www.gsmarena.com/makers.php3",
                           "http://www.gsmarena.com/acer-phones-59.php",
                           "http://www.gsmarena.com/alcatel-phones-5.php"                            ]
        #self.start_urls = self.get_urls_from_solr()
        self.count = 0
        self.deny = ""
        self.crawl_limt = 0
        self.real_count = 0
        self.batch_size = 300
        self.mobile_product = []

    def parse_custom(self, response):
        """ Parse the response """

        #self.parse(response)
        # content = response.body
        content = response
        content = content.body
        # content = unicode(content, errors='ignore')
        # content = bleach.clean(content)
        # self.logger.nfo('Parse function called on %s', response.url)
        mobile_json = content_parser(content,response.url)
        if mobile_json:
            self.count = self.count+1
            # print mobile_json
            self.mobile_product.extend(mobile_json)
            # print self.mobile_product
            if self.count % self.batch_size == 0 and self.mobile_product:
                f = open('mobiledata.json', 'w')
                f.write(json.dumps(self.mobile_product))
                f.close()
                # print "Written => ",self.mobile_product
                print ("Product written to file => ",self.count, end='\r')
            # self.mobile_product.append(mobile_json)
        # print "######## URL IS==> ",product_url
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
        # self.count += 1

        print ("Product Found => ", self.count, end='\r')
        # print "Totoal product =>",len(self.mobile_product)
        # if self.real_count > self.crawl_limt:
        #     raise CloseSpider('crawl limit ==>>done')