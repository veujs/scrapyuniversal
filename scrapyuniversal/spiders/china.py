# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from ..items import NewsItem

from scrapyuniversal.loader import ChinaLoader
from scrapyuniversal.rules import rules


class ChinaSpider(CrawlSpider):
    # def __init__(self):
    #     print("111111111111111111111111111111111111111111111111111111111111111111111111111")
    #     super(ChinaSpider, self).__init__()
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['http://tech.china.com/articles/']
    rules = rules

    def parse_item(self, response):
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]//text()')
        loader.add_xpath('datetime', '//div[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//div[@id="chan_newsInfo"]/text()', re='来源：(.*)')
        loader.add_value('website', "中华网")
        yield loader.load_item()

        # item = NewsItem()
        # item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        # item['url'] = response.url
        # item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]//text()').extract()).strip()
        # item['datetime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
        # item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('来源：(.*)').strip()
        # item['website'] = "中华网"
        #
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # yield item
