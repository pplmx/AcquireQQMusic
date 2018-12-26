#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 12/26/2018 21:09
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "2scrape-css"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

