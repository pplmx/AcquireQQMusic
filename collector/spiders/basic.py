# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    # Function start_requests is the same as Variable start_urls
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # exercise 1
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        # exercise 2
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
            # Solution 1
            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
            # # Solution 2
            # # You can also pass a selector to response.follow instead of a string;
            # # this selector should extract necessary attributes:
            # for href in response.css('li.next a::attr(href)'):
            #     yield response.follow(href, callback=self.parse)
            # # Solution 3
            # # For <a> elements there is a shortcut:
            # # response.follow uses their href attribute automatically.
            # # So the code can be shortened further:
            # for a in response.css('li.next a'):
            #     yield response.follow(a, callback=self.parse)
