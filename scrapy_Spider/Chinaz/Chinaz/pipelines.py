3  # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json, os
import pymysql
import scrapy
import pymongo
from Chinaz.items import ChinazWebinfoItem, ChinazTagItem
from scrapy.utils.project import get_project_settings
from scrapy.contrib.pipeline.images import ImagesPipeline


images_store = get_project_settings().get('IMAGES_STORE')


class ChinazImagesPipeline(ImagesPipeline):
    # 实现2个方法

    def get_media_requests(self, item, info):
        """
        根据图片url地址发起请求
        :param item:
        :param info:
        :return:
        """
        if isinstance(item, ChinazWebinfoItem):
            image_url = item['CoverImage']
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        """
        图片下载
        :param results: 响应结果,True是成功,False是失败。{'path':'图片下载后的存储路径','url':'图片的url地址','ckecksum':'经过hash加密的一个字符串'}
        :param item: 
        :param info: 
        :return:
        """
        paths = [result['path'] for status, result in results if status]
        print('图片下载结果：', results)
        if len(paths) > 0:
            print('图片下载成功')
            os.rename(images_store + '/' + paths[0], images_store + '/full' + '/' + item['Title'] + '.jpg')
            image_path = images_store + '/' + item['Title'] + '.jpg'
            item['localImagePath'] = image_path
        else:
            # 如果没有成功获取图片,将这个item丢弃
            # from scrapy.exceptions import DropItem
            # raise DropItem('没有获取到图片')
            return item

        return item


# # mongo数据库存储数据
# class ChinazPipeline(object):
#
#
#     def __init__(self,host,port,db):
#         # 创建mongodb的数据库链接
#         self.mongo_client = pymongo.MongoClient(host=host,port=port)
#
#         self.db = self.mongo_client[db]
#
#     @classmethod
#     def from_crawler(cls,crawler):
#         """
#         MONGO_HOST = '127.0.0.1'
#         MONGO_PORT = 27017
#         MONGO_DB = 'chinaz'
#         :param crawler:
#         :return:
#         """
#         host = crawler.settings['MONGO_HOST']
#         port = crawler.settings['MONGO_PORT']
#         db = crawler.settings['MONGO_DB']
#         return cls(host,port,db)
#
#     def open_spider(self,spider):
#         print(spider.name,'：爬虫开始运行！！！')
#
#     def process_item(self, item, spider):
#
#         # 往哪个集合插入数据
#         # 往集合下面插入那些数据
#
#         data_dict = dict(item)
#
#         col_name = item.get_mongo_collectionName()
#         col = self.db[col_name]
#         col.insert(data_dict)
#
#
#         return item
#
#     def close_spider(self,spider):
#         self.mongo_client.close()
#         print('爬虫结束')


# # mysql数据库存储数据
# class ChinazPipeline(object):
#     def __init__(self):
#         """
#         初始化方法
#         """
#         # self.file = open('chinaz.json','a')
#         self.connect = pymysql.Connect('127.0.0.1', 'root', 'abcd1234', '1712B', 3306, charset='utf8')
#         self.cursor = self.connect.cursor()
#
#     def open_spider(self, spider):
#         """
#         爬虫启动的时候会调用一次
#         :param spider:
#         :return:
#         """
#         print('开启爬虫！！！')
#
#     def process_item(self, item, spider):
#         """
#         这个方法是必须实现的，爬虫文件中所有的item都会经过这个方法
#         :param item: 爬虫文件传递过来的item对象
#         :param spider: 爬虫文件实例化的对象
#         :return:
#         """
#         # # 存储到本地json文件
#         # data_dict = dict(item)
#         # # json_data = json.dumps(data_dict,ensure_ascii=False)
#         # # self.file.write(json_data+'\n')
#
#         # data_dict = dict(item)
#         # sql, data = item.get_insert_sql_data(data_dict)
#
#         # if isinstance(item, ChinazWebinfoItem):
#         #     print('网站信息')
#         #     table = 'Webinfo'
#         # elif isinstance(item, ChinazTagItem):
#         #     table = 'tags'
#         #
#         # keys = ','.join(data_dict.keys())
#         # sql = """INSERT INTO {tables}({columns}) values ({values})""".format(tables=table, columns=keys,
#         #                                                                      values=(','.join(["%s"] * len(data_dict))))
#         self.cursor.execute(sql, data)
#         self.connect.commit()
#         # 如果有多个管道文件，一定要注意return item,否则下一个管道无法接收到item
#         print('经过管道')
#
#         return item
#
#     def close_spider(self, spider):
#         """
#         爬虫结束的时候会调用一次
#         :param spider:
#         :return:
#         """
#         self.cursor.close()
#         self.connect.close()
#         print('结束爬虫！！！')


# 实现mysql数据库的异步插入(要插入的数据量非常大的情况下)
from twisted.enterprise import adbapi


class ChinazPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_crawler(cls, cralwer):
        db_parmars = {
            'host': cralwer.settings['MYSQL_HOST'],
            'user': cralwer.settings['MYSQL_USER'],
            'passwd': cralwer.settings['MYSQL_PWD'],
            'db': cralwer.settings['MYSQL_DB'],
            'port': cralwer.settings['MYSQL_PORT'],
            'charset': cralwer.settings['MYSQL_CHARSET'],
        }
        dbpool = adbapi.ConnectionPool('pymysql', **db_parmars)

        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(
            self.insert_data_to_mysql, item
        )
        query.addErrback(
            self.insert_err, item
        )
        return item

    def insert_data_to_mysql(self, cursor, item):
        data_dict = dict(item)
        sql, data = item.get_insert_sql_data(data_dict)
        cursor.execute(sql, data)

    def insert_err(self, failure, item):
        print(failure, '插入失败', item)
