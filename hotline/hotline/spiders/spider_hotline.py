# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from ..items import HotlineItem
from scrapy.linkextractors import LinkExtractor
from urlparse import urljoin

class HotlineSpider(CrawlSpider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["http://hotline.ua/mobile/mobilnye-telefony-i-smartfony/"]

    rules = [
        Rule(LinkExtractor(restrict_xpaths=("//*[@id='catalogue']/ul/li/div/div/div/a" )),  # "//*[@id='catalogue']/div/span/a",
             callback='parse_item', follow=True),

    ]

    def get_value(self, xpath):
        result = xpath.extract()
        if len(result) == 1:
            return ''.join(result[0]).strip()
        elif len(result) > 1:
            for i, item in enumerate(result):
                result[i] = item.strip()
            return ''.join(result)
        else:
            return "None"

    def parse_item(self, response):
        self.logger.info('Parse starting for %s' % response.url)
        hxs = response
        item = HotlineItem()
        item['name'] = self.get_value(hxs.xpath('/html/body/div/div/div/div/h1/text()'))
        item['description'] = self.get_value(hxs.xpath('/html/body/div/div/div/div/div/div/div/div/p/text()'))
        item['average_price'] = self.get_value(hxs.xpath('/html/body/div/div/div/div/div/div/div/div/div/div/span/span/text()'))
        item['price'] = self.get_value(hxs.xpath('/html/body/div/div/div/div/div/div/div/div/div/div/span/span/strong/text()'))
        item['shop'] = self.get_value(hxs.xpath('/html/body/div/div/div/div/div/ul/li/noindex/a/@href'))

        for link in response.xpath('/html/body/div/div/div/div/div/div/span/a/@href').extract():
            if link.endswith('/?tab=3'):

                request = scrapy.Request(url=urljoin(response.url, link.strip()), callback=self.parse_rewiew2)

                request.meta['item'] = item
                return request


    def parse_rewiew2(self, response):
        for link in response.xpath('/html/body/div/div/div/div/div/div/span/a/@href').extract():
            if link.endswith('?tab=3&show=reviews'):
                request = scrapy.Request(url=urljoin(response.url, link.strip()), callback=self.parse_list)
                request.meta['item'] = response.meta['item']
                return request

    def parse_list(self, response):
        hxs = response
        item = response.meta['item']
        item['rewiew'] = self.get_value(hxs.xpath('/html/body/div/div/div/div/div/ul/li/div/p/text()'))
        return item

