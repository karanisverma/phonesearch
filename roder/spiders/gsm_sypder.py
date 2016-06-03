from __future__ import print_function
import json
from content_parser import content_parser
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


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

    custom_settings = {"HTTP_ENABLED": True,
                       "HTTP_PROXY": "http://183.207.228.122:80"}

    def __init__(self):
        self.domain = "www.gsmarena.com"
        self.name = "gsmarena"
        self.custom_settings = {}
        self.allowed_domains = ["www.gsmarena.com"]
        CrawlSpider.__init__(self)
        self.start_urls = ["http://www.gsmarena.com/makers.php3",
                           "http://www.gsmarena.com/acer-phones-59.php",
                           "http://www.gsmarena.com/alcatel-phones-5.php"]
        self.count = 0
        self.deny = ""
        self.crawl_limt = 0
        self.real_count = 0
        self.batch_size = 300
        self.mobile_product = []

    def parse_custom(self, response):
        """ Parse the response """
        content = response
        content = content.body
        mobile_json = content_parser(content, response.url)
        if mobile_json:
            self.count = self.count + 1
            # print mobile_json
            if self.count % self.batch_size == 0 and self.mobile_product:
                f = open('mobiledata.json', 'w')
                f.write(json.dumps(self.mobile_product))
                f.close()
                print ("Product written to file => ", self.count, end='\r')
        print ("Product Found => ", self.count, end='\r')
