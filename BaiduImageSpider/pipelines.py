# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class BaiduimagespiderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['img_url']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        # rewrite the file_path
        virtual = request.meta['item']['virtual']
        img_class = request.meta['item']['img_class']
        img_index = request.meta['item']['img_index']
        filename = u'{0}/{1}/{2}.jpg'.format(virtual,img_class, img_index)
        return filename
