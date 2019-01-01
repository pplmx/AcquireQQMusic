# -*- coding: utf-8 -*-
import json
from urllib import parse

import scrapy
from scrapy.spiders import CrawlSpider

from collector.items import SingerItem, SongItem


class AdaCrawlSpider(CrawlSpider):

    def __init__(self, singer=None):
        super(AdaCrawlSpider, self).__init__()
        self.__singer = singer

    # https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E8%AE%B8%E5%B5%A9
    # https://y.qq.com/n/yqq/singer/000CK5xN3yZDJt.html
    # https://y.qq.com/n/yqq/song/004Sktnw0KnoIF.html
    # https://y.qq.com/n/yqq/mv/v/y00119yn6bd.html

    name = 'Ada'
    allowed_domains = ['qq.com']
    start_urls = [
        'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=0&new_json=1'
        '&remoteplace=txt.yqq.center&searchid=0&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0'
        '&{p_page_idx}'
        '&{n_page_no}'
        '&{w_singer}'
        '&g_tk=0&jsonpCallback=MusicJsonCallback9260186144153801&loginUin=0&hostUin=0'
        '&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewC',
    ]

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://y.qq.com/portal/search.html"
    }

    singer_url = 'https://y.qq.com/n/yqq/singer/{singer_mid}.html'
    song_url = 'https://y.qq.com/n/yqq/song/{song_mid}.html'
    mv_url = 'https://y.qq.com/n/yqq/mv/v/{song_vid}.html'

    page_idx = 1
    page_no = 20

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0].format(
            p_page_idx=parse.urlencode({'p': self.page_idx}),
            n_page_no=parse.urlencode({'n': self.page_no}),
            w_singer=parse.urlencode({'w': self.__singer})
        ), callback=self.parse_singer)

    # rules = (
    #     Rule(LinkExtractor(allow=r'https://y.qq.com/n/yqq/singer/.+'), callback='parse_item', follow=True),
    # )

    def parse_singer(self, response):
        resp = response.body[34: -1]
        with open("%s.json" % self.__singer, 'wb') as f:
            f.write(resp)
        result = json.loads(resp)
        singer = SingerItem()
        song = SongItem()
        # the difference between dict.get(key) and dict[key]
        singer['singer_id'] = result['data']['zhida']['zhida_singer']['singerID']
        singer['singer_mid'] = result['data']['zhida']['zhida_singer']['singerMID']
        singer['singer_name'] = result['data']['zhida']['zhida_singer']['singerName']
        singer['singer_pic'] = result['data']['zhida']['zhida_singer']['singerPic']
        singer['singer_album_num'] = result['data']['zhida']['zhida_singer']['albumNum']
        singer['singer_mv_num'] = result['data']['zhida']['zhida_singer']['mvNum']
        singer['singer_song_num'] = result['data']['zhida']['zhida_singer']['songNum']
        singer['singer_authorized2qq_num'] = result['data']['song']['totalnum']
        yield singer
        for i in self.song_generator(song, result):
            yield scrapy.Request(self.song_url.format(singer_mid=i['song_mid']), callback=self.parse_song)
        # next page
        for i in range(2, int(singer['singer_authorized2qq_num']) // self.page_no + 2):
            yield scrapy.Request(self.start_urls[0].format(
                p_page_idx=parse.urlencode({'p': i}),
                n_page_no=parse.urlencode({'n': self.page_no}),
                w_singer=parse.urlencode({'w': self.__singer})
            ), callback=self.parse)

    def parse_song(self, response):

        pass

    # noinspection PyMethodMayBeStatic
    def song_generator(self, song, result):
        for i in result['data']['song']['list']:
            song['song_mid'] = i['mid']
            song['song_name'] = i['name']
            song['song_vid'] = i['mv']['vid']
            song['song_publish'] = i['time_public']
            yield song
