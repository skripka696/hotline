# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from ..items import HotlineItem
from scrapy.linkextractors import LinkExtractor


class HotlineSpider(CrawlSpider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["http://hotline.ua/mobile/mobilnye-telefony-i-smartfony/"]
    # rules = [
    #     Rule
    #     (
    #         LinkExtractor(
    #             restrict_xpaths=("//*[@id='catalogue']/div/span/a")),
    #         callback = 'parse_item',
    #         follow = True,
    #     ),
    #
    #     # Rule
    #     # (
    #     #     LinkExtractor(
    #     #         restrict_xpaths=("//*[@id='catalogue']/ul/li/div/div/div/a")),
    #     #     callback = 'parse_phone',
    #     #     follow = True,
    #     # )
    # ]
    #
    # def parse_item(self, response):
    #     hxs = response
    #     item = HotlineItem()
    #     item['name'] = hxs.xpath('//*[@id="catalogue"]/ul/li/div/div/div/a/text()').extract()
    #     item['payment'] = hxs.xpath('//*[@id="catalogue"]/ul/li/div/span[@class="orng"]/text()').extract()
    #     print item
    #     return item
    #
    # # def parse_phone(self, response):
    # #     hxs = response
    # #     item = HotlineItem()
    # #     item['price'] = hxs.xpath('/html/body/div/div/div/div/div/div/div/div/div/div/span/a[@class="orng g_statistic"]/text()').extract()
    # #
    # #     print item
    # #     return item
    rules = [
        Rule(LinkExtractor(restrict_xpaths=("//*[@id='catalogue']/ul/li/div/div/div/a", )),  # "//*[@id='catalogue']/div/span/a",
             callback='parse_item', follow=True),

        # Rule(LinkExtractor(
        #     restrict_xpaths=("//*[@id='catalogue']/ul/li/div/div/div/a", )),
        #     callback='parse_description', follow=True)
    ]

    def parse_item(self, response):
        hxs = response
        item = HotlineItem()
        item['name'] = hxs.xpath('/html/body/div/div/div/div/h1/text()').extract()[0].strip()
        print item['name']
        item['description'] = hxs.xpath('/html/body/div/div/div/div/div/div/div/div/p/text()').extract()[0].strip()
        yield item

    # def parse_description(self, response):
    #     hxs = response
    #     item = HotlineItem()
    #
    #     item['description'] = hxs.xpath(
    #         '/html/body/div/div/div/div/div/div/div/div/p/text()').extract()
    #     print type(hxs.xpath(
    #         '/html/body/div/div/div/div/div/div/div/div/p/text()').extract()[0])
    #     yield item
