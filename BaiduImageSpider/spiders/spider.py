#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/6/8 22:59
# @Author : LiFH
# @Site : 
# @File : spider.py
# @Software: PyCharm Community Edition
import scrapy
import json
from BaiduImageSpider.items import BaiduimagespiderItem
import csv
import urllib


import sys
reload(sys)
sys.setdefaultencoding('utf8')
filename = 'labels.txt'
class BaiduImageSpider(scrapy.Spider):
    name = "baiduSpider"
    start_urls = []
    def start_requests(self):
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                # print line
                line = line.split(',')
                queryWord = line[1] + line[2]
                for i in range(0, 1, 1):
                    url = 'https://image.baidu.com/search/acjson' \
                          '?tn=resultjson_com&ipn=rj&ct=201326592' \
                          '&is=&fp=result&queryWord=' + queryWord + \
                          '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0' \
                          '&word=' + queryWord + '&s=&se=&tab=&width=&height=' \
                                                 '&rn=1&face=0&istype=2&qc=&nc=1&fr=&pn=%d' % i
                    request = scrapy.Request(url
                                             , callback=self.parse
                                             , meta={'class_id': line[0]
                                                    , 'class': line[1]
                                                    , 'virtual': line[2]})
                    yield request

    def parse(self, response):
        imgs = json.loads(response.body)['data']
        index = 1
        for img in imgs:
            item = BaiduimagespiderItem()
            try:
                item['img_url'] = [img['middleURL']]
                item['img_class'] = response.meta['class']
                item['class_id'] = response.meta['class_id']
                item['img_index'] = index
                item['virtual'] = response.meta['virtual']
                index = index + 1
                yield item
            except Exception as e:
                print
                e
