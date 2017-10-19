# -*- coding: utf-8 -*-
__author__ = 'shentao'
import scrapy
from scrapy.http import Request

from JiashanRencai.items import PeopleItem
import json


class BaiduimageSpider(scrapy.Spider):
    name = 'baiduimage'
    allowed_domains = ['image.baidu.com']

    pages = 100
    keywords = list(set(['日本人']))

    def start_requests(self):
        for key_word in self.keywords:

            for i in range(30, 30 * self.pages + 30, 30):
                requests_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%8A%9E%E5%85%AC%E5%AE%A4&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={0}=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={1}&rn=30&gsm=5a&1508398887415='.format(
                    key_word, i)
                yield Request(
                    url=requests_url,
                    callback=self.parse_key_image)

    def parse_key_image(self, response):
        People_Item = PeopleItem()
        response_json = json.loads(response.text)
        for image_data in response_json['data']:
            People_Item["image_urls"] = image_data['thumbURL']
            yield People_Item
