# -*- coding: utf-8 -*-
from urllib import parse

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AdaCrawlSpider(CrawlSpider):

    def __init__(self, singer=None):
        super(AdaCrawlSpider, self).__init__()
        self.start_urls = [
            'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&%s'
            % parse.urlencode({'w': singer})
        ]

    name = 'Ada'
    allowed_domains = ['qq.com']

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://y.qq.com/portal/search.html"
    }

    rules = (
        Rule(LinkExtractor(allow=r'https://y.qq.com/n/yqq/singer/.+'), callback='parse_item', follow=True),
    )

    # noinspection PyMethodMayBeStatic
    def parse_item(self, response):
        with open("search2.html", 'wb') as f:
            f.write(response.body)
        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
