__author__ = 'bogus'

import scrapy

class DmozSpider(scrapy.Spider):
    name = "naver"
    allowed_domains = ["naver.com"]
    start_urls = [
        "http://www.naver.com"
        
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print (title, link, desc)