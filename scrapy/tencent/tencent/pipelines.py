# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
import pymysql
class TencentPipeline(object):
    # 链接mongodb数据库
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.tencent
        self.jobs = self.db.jobs
    # 写入本地json
    # def __init__(self):
    #     self.file = open('job.json','a+')
    # 链接pymysql数据库
    # def __init__(self):
    #     # 链接数据库
    #     self.client = pymysql.Connect('localhost','root','')
    #     # 创建游标，执行sql语句
    #     self.cursor = self.client.cursor()

    def process_item(self, item, spider):

        json_str = json.dumps(dict(item),ensure_ascii=False) + '\n'
        # self.file.write(json_str)
        # 插入mongodb数据库
        # 先将数转换成ditc类型，再把数据放入mongodb
        self.jobs.insert(dict(item))
        # pymysql
        # insert_sql = "INSERT INTO jobs(jobName,workLocation,jobType,jobDesc,jobInfo) VALUE(%s,%s,%s,%s,%s)"
        # self.cursor.execute(insert_sql,(item['jobName']),(item['workLocation']),(item['jobType']),(item['jobDesc']),(item['jobInfo']))
        # self.client.close()
        return item
    # def close_file(self):
    #     self.file.close()