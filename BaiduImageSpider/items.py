# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduimagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_url = scrapy.Field()  # 图像所对应url
    img_class = scrapy.Field()  # 图像所对应类别
    img_index = scrapy.Field()  # 序号
    pass

