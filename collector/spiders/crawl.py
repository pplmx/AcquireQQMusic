# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AdaCrawlSpider(CrawlSpider):

    def __init__(self, singer=None):
        super(AdaCrawlSpider, self).__init__()
        self.__singer = singer

    # https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E8%AE%B8%E5%B5%A9
    # https://y.qq.com/n/yqq/singer/000CK5xN3yZDJt.html

    name = 'Ada'
    allowed_domains = ['qq.com']
    start_urls = ['https://c.y.qq.com/soso/fcgi-bin/client_search_cp']

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://y.qq.com/portal/search.html"
    }

    def start_requests(self):
        yield scrapy.Request(url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp', meta={
            "ct": "24",
            "qqmusic_ver": "1298",
            "new_json": "1",
            "remoteplace": "txt.yqq.top",
            "searchid": "21871562692607763",
            "t": "0",
            "aggr": "1",
            "cr": "1",
            "catZhida": "1",
            "lossless": "0",
            "flag_qc": "0",
            "p": "1",
            "n": "20",
            "w": self.__singer,
            "g_tk": "5381",
            "loginUin": "0",
            "hostUin": "0",
            "format": "json",
            "inCharset": "utf8",
            "outCharset": "utf - 8",
            "notice": "0",
            "platform": "yqq.json",
            "needNewCode": "0",
            }, callback=self.parse)

    # rules = (
    #     Rule(LinkExtractor(allow=r'https://y.qq.com/n/yqq/singer/.+'), callback='parse_item', follow=True),
    # )

    # noinspection PyMethodMayBeStatic
    def parse(self, response):
        with open("search2.html", 'wb') as f:
            f.write(response.body)
        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
