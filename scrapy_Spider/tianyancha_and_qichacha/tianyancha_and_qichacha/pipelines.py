# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi


class TianyanchaAndQichachaPipeline(object):
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

    def insert_data_to_mysql(self, cursor, item):
        dict_data = dict(item)
        sql, data = item.get_data_save_to_db(dict_data)
        cursor.execute(sql, data)
        print('插入成功')
    def insert_err(self, failure, item):
        print(failure, '插入失败', item)
