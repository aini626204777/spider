# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class BaidulvyouPipeline(object):
    def __init__(self):
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        mydb = settings['MONGO_DB']
        cooection = settings['MONGO_COLLECTION']

        client = pymongo.MongoClient(host=host, port=port)
        my_DB = client[mydb]
        self.collections = my_DB[cooection]

    def process_item(self, item, spider):
        content = dict(item)
        self.collections.insert(content)
        return item
