#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 1/6/2019 13:08
import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ['qq.com']

    start_urls = [
        'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E8%AE%B8%E5%B5%A9',
    ]

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    def parse(self, response):
        with open("response.html", 'wb') as f:
            f.write(response.body)
