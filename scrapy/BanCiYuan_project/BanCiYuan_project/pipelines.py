# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.cmdline import get_project_settings
import os
import pymongo

class img_load(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        self.img_url = item['image_path']
        for fullurl in self.img_url:
            yield scrapy.Request(fullurl)

    def item_completed(self, results, item, info):

        for key, value in results:
            if key:
                img = value['path']
                os.rename(self.IMAGES_STORE + '/' + img,self.IMAGES_STORE+'/'+item['name']+'.jpg')
                item['load_image'] = self.IMAGES_STORE+'/'+item['name']+'.jpg'
                return item


class BanciyuanProjectPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient('localhost',27017)
        self.bcy_db = self.client.BanCiYuan
        self.bcy = self.bcy_db.banciyuan

    def open(self):
        print('开始你的项目')

    def process_item(self, item, spider):
        self.bcy.insert(dict(item))

    def close(self):
        print('运行安全结束')