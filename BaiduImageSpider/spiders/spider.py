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
import  urllib

filename = 'labels.csv'

class BaiduImageSpider(scrapy.Spider):
    name = "baiduSpider"

    start_urls = []
    with open(filename) as f:
        # 创建cvs文件读取器
        reader = csv.reader(f)
        for line in reader:
            word = line[1] + line[2]
            start_urls += [
                'https://image.baidu.com/search/acjson' \
                '?tn=resultjson_com&ipn=rj&ct=201326592' \
                '&is=&fp=result&queryWord=' + word + \
                '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0' \
                '&word=' + word + '&s=&se=&tab=&width=&height=' \
                                  '&rn=1&face=0&istype=2&qc=&nc=1&fr=&pn=%d' % i
                for i in range(0, 1, 1)
            ]

    def parse(self, response):
        imgs = json.loads(response.body)['data']
        # print '----------------------------------'
        queryEnc = json.loads(response.body)['queryExt']
        # print '----------------------------------'
        # print(imgs)
        index = 1
        for img in imgs:
            item = BaiduimagespiderItem()
            try:
                item['img_url'] = [img['middleURL']]
                item['img_class'] = urllib.unquote(queryEnc)
                item['img_index'] = index
                index = index + 1

                yield item
            except Exception as e:
                print e
