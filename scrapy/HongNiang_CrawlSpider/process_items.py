import redis
import pymongo
import json


def main():
    mongoclient = pymongo.MongoClient('localhost',27017)
    rediscli = redis.StrictRedis('localhost',6379,0)

    # 拿到mongodb里面的数据路
    db = mongoclient['HongNiang']
    # 拿到数据库中的集合
    HN = db['hn']

    while True:
        source,data = rediscli.blpop(['HongNiang:items'])
        data = data.decode('utf8')
        data = json.loads(data)
        HN.insert(data)

if __name__ == '__main__':
    main()