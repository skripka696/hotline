# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from ..items import HotlineItem
from scrapy.linkextractors import LinkExtractor


class HotlineSpider(CrawlSpider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["http://hotline.ua/mobile/mobilnye-telefony-i-smartfony/"]
    rules = [
        Rule
        (
            LinkExtractor(
                restrict_xpaths=("//*[@id='catalogue']/div/span/a")),
            callback = 'parse_item',
            follow = True,
        )
    ]

    def parse_item(self, response):
        hxs = response
        item = HotlineItem()
        item['name'] = hxs.xpath('//*[@id="catalogue"]/ul/li/div/div/div/a/text()').extract()
        item['payment'] = hxs.xpath('//*[@id="catalogue"]/ul/li/div/span/i/text()').extract()
        print item
        return item
