# -*- coding:utf-8 -*-
import pymongo

# 链接mongodb数据库

# 链接方式
client = pymongo.MongoClient('localhost',27017)
client1 = pymongo.MongoClient('127.0.0.1',27017)

# 远程链接
client2 = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# 如何获取数据库
article_db = client.article

# 获取数据库下面的集合
articlenovel = article_db.articlenove1

# 查询所有的数据文档
results = articlenovel.find()

# 读取结果中的所有文档数据
# for i in results:
#     print(i)

db = client.meinv
model = db.model
document = {
    'name':'tianjing',
    'age':'20',
    'class':'201',
    'hight':165,
}
document1 = {
    'name':'tianjing',
    'age':'21',
    'class':'204',
    'hight':170,
}
document2 = {
    'name':'tianjing4',
    'age':'22',
    'class':'202',
    'hight':160,
}

# result = model.insert([document1,document2])
a = model.find()
for i in a:
    # print(i)
    pass
# 获取第一条满足条件的数据
# result = model.find_one()
# print(result)

# 跳过第一条数据获取后面所有的数据
result1 = model.find().skip(1)
for i in result1:
    # print(i)
    pass
result2 = model.find().skip(1).limit(2)
for i in result2:
    # print(i)
    pass

# 更新
# a = model.update({'name':'tianjing4'},{'$set':{'hight':177}})
# result3 = model.find_one({"hight":177})
# print(result3)

# 升序
result4 = model.find().sort('age',1)
for i in result4:
    # print(i)
    pass
result5 = model.find().sort('age',-1)
for i in result5:
    # print(i)
    pass

# save跟update区别是什么？
# 如果update更新的内容（_id)在集合中不存在，就无法更新
# 如果save跟新的内容(_id)在集合中不存在，就会直接插入一条新数据