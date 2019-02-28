import json
import redis
import pymongo


# def get_data_to_mongoDB():
#     # 指定Redis数据库信息
#     redis_cli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
#     # 指定MongoDB数据库信息
#     mongocli = pymongo.MongoClient(host='localhost', port=27017)
#     # 指定数据库
#     db = mongocli['xcfdb']
#     # 指定集合
#     sheet = db['xcfcol']
#     while True:
#         # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
#         source, data = redis_cli.blpop("xcfCrawlSpider:items", timeout=3)
#         data = data.decode('utf-8')
#         item = json.loads(data)
#
#         try:
#             sheet.insert(item)
#             print("Processing:insert successed" % item)
#         except Exception as err:
#             print("err procesing: %r" % item)
#
#
# if __name__ == '__main__':
#     get_data_to_mongoDB()

import json
import redis
import pymysql

def get_data_to_mongoDB():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='localhost', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='localhost', user='用户', passwd='密码', db = '数据库', port=3306, use_unicode=True)
    # 使用cursor()方法获取操作游标
    cur = mysqlcli.cursor()

    while True:

        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop("redis中对应的文件夹:items")
        item = json.loads(data.decode('utf-8'))

        try:

            keys = ','.join(item.keys())
            sql = """INSERT INTO xcfdata({columns}) values ({values})""".format(columns=keys,values=(','.join(["%s"] * len(item))))
            data = list(item.values())
            # 使用execute方法执行SQL INSERT语句
            cur.execute(sql,data)

            # 提交sql事务
            mysqlcli.commit()

            print("inserted successed")

        except Exception as err:
            #插入失败
            print("Mysql Error",err)
            mysqlcli.rollback()

if __name__ == '__main__':
    get_data_to_mongoDB()
