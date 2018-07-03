# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

class db(ImagesPipeline):

    def get_media_requests(self, item, info):
        img_url = item['coverImage']
        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        for ok, x in results:
            if ok:
                i = x['path']
                item['image_load'] = i
                return item


class JobboleProjectPipeline(object):
#     def __init__(self):
#         self.client = pymysql.Connect('localhost', 'root', 'ljh123456', 'jobbole', 3306, charset='utf8')
#         self.cursor = self.client.cursor()
#
#     def open_spider(self, spider):
#         # 在这也可以写数据库信息
#         # spider文件开始执行就会执行这个方法
#         print('open_spider')
#
    def process_item(self, item, spider):
        pass
#         insert_sql = """
#                INSERT INTO article(coverImage,title,publishTime,content,tags,url) VALUES(%s,%s,%s,%s,%s,%s)
#             """
#         self.cursor.execute(insert_sql, (item['coverImage'], item['title'],
#                                          item['publishTime'], item['content'],
#                                          item['tags'], item['url'])
#                             )
#         self.client.commit()
#
#         return item
#
#     def close_spider(self, spider):
#         # 爬虫任务全部执行完毕，就会执行这个方法
#         self.cursor.close()
#         self.client.close()

# class JobboleprojectFilePipeline(object):
#
#     def __init__(self):
#         self.client = pymysql.Connect('localhost', 'root', 'ljh123456', 'jobbole', 3306, charset='utf8')
#         self.cursor = self.client.cursor()
#
#     def open_spider(self, spider):
#         # 在这也可以写数据库信息
#         # spider文件开始执行就会执行这个方法
#         print('open_spider')
#
#     def process_item(self, item, spider):
#         insert_sql = """
#            INSERT INTO article(coverImage,title,publishTime,content,tags,url) VALUES(%s,%s,%s,%s,%s,%s)
#         """
#         self.cursor.execute(insert_sql, (item['coverImage'], item['title'],
#                                          item['publishTime'], item['content'],
#                                          item['tags'], item['url'])
#                             )
#         self.client.commit()
#
#         return item
#
#     def close_spider(self, spider):
#         # 爬虫任务全部执行完毕，就会执行这个方法
#         self.cursor.close()
#         self.client.close()
