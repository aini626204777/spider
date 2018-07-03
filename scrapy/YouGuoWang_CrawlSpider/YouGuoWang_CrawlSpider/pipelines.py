# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from scrapy.cmdline import get_project_settings
from scrapy.conf import settings
import pymongo


class download_iamge(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        img_url = item['img_path']
        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        # print(results)
        for key, vlaue in results:
            if key:
                img_path = vlaue['path']
                # print(item['title'])
                os.rename(self.IMAGES_STORE + '/' + img_path,
                          self.IMAGES_STORE + '/' + item['title'] + item['name'] + '.jpg')
                item['img_load_path'] = self.IMAGES_STORE + '/' + item['title'] + item['name'] + '.jpg'
                return item


class YouguowangCrawlspiderPipeline(object):
    def __init__(self):
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        mydb = settings['MONGO_DB']
        collections = settings['MONGO_COLLECTIONS']

        # 链接mongo数据库
        client = pymongo.MongoClient(host=host, port=port)
        db = client[mydb]
        self.collections = db[collections]

    def process_item(self, item, spider):
        print(item)
        content = dict(item)
        self.collections.insert(content)
        return item
