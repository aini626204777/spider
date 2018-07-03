# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from jobbole.items import JobboleItem

# class jo(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         # 根据图片链接构造Requests，给调度器，放在任务队列里面
#         image_url = item['coverImageLocalPath']
#         yield scrapy.Request(image_url, )
#
#     # 图片下载成功之后会调用这个函数
#     def item_completed(self, results, item, info):
#         # 图片任务下载完成之后会执行这个方法
#         for ok,x in results:
#             if ok:
#                 image_path = x['path']
#                 item['coverImageLocalPath'] = image_path
#                 return item



class JobbolePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.jobble
        self.jobbleCl = self.db.jobbleCl

    def open_spider(self, spider):
        print('开始插入数据')

    def process_item(self, item, spider):
        self.jobbleCl.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
        print('执行结束了')
