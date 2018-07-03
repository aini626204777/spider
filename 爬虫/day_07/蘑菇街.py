# -*- coding:utf-8 -*-
import requests
import re
import json
import csv
import pymysql


# http://www.mogujie.com/
# 首先发现获取的首页为空的html，没有我们想要的数据
# 但是网页上出现了，说明数据肯定通过接口加载出来了

# 这个接口是获取大分类的接口
# http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery2110055639624415818045_1528697742318
# &pids=110119&_=1528697742319

# http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery2110055639624415818045_1528697742318
# &pids=109499,109520,109731,109753,110549,109779,110548,110547,109757,109793,109795,110563,110546,110544&_=1528697742322

# 定义这个方法是为了获取所有的分类
def get_all_category():
    # 定一个变量承接目标网址,要获取最大分类的id
    url = 'https://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery211044757024852998817_1528700498354&pids=110119&_=1528700498355'
    # 请求目标网址
    request = requests.get(url=url)
    # 获取目标网址文本内容
    html = request.text
    # 创建一个正则对象，去匹配返回结果的json字符串
    pattern = re.compile('jQuery.*?\((.*?)\)')
    # 获取用正则匹配到的内容
    json_data = re.findall(pattern, html)[0]
    # print(json_data)
    # 获取的json字符串，转换成python对象
    data = json.loads(json_data)
    # print(type(data))
    # 取最大分类的分类列表
    big_ategory = data['data']['110119']['list']
    # print(big_ategory)
    # 定义一个控列表,用来装最大分类的id
    pids = []
    # 创建一个for循环，遍历最大分类的列表
    for item in big_ategory:
        # 把categoryPid添加到实现县准备好的列表里
        pids.append(item['categoryPid'])
    # 将pids列表以都好分隔拼接成一个字符串
    pids = ','.join(pids)
    # print(pids)

    # 确认第二分类的目标网址
    url = 'https://mce.mogucdn.com/jsonp/multiget/3?'
    # 确认第二分类的参数，并把上面获取的id添加到里边
    parmas = {
        'callback': 'jQuery21102211810244577579_1528698251813',
        'pids': pids,
        '_': '1528698251817'
    }
    # 　请求目标第二分类网址
    response = requests.get(url=url, params=parmas)
    # print(response.text)
    # 获取需要正则匹配到的内容
    json_data2 = re.findall(pattern, response.text)[0]
    # print(json_data2)
    # 匹配到的内容是json字符串，转换成python对象
    data2 = json.loads(json_data2)
    # print(data2)
    # 获取所有分类的数据信心
    big_ategory2 = data2['data']
    # print(big_ategory2)
    # 使用正则匹配与分类连接的id
    category_pattern = re.compile('http.*?/(\d+)\?acm', re.S)
    # 创建category_dict来存放数据，category_dict为字典类型数据
    category_dict = {}
    # 创建user_categorys来存放菜单栏列表，user_categorys为list
    user_category_list = []
    # for循环遍历将菜单的标题和id取出，
    # title放入user_categorys后面将这个列表展示给用户，形成一个菜单栏
    # 将分类title和id以键值的形式存放在category_dict字典中，方便后面直接根据title取出对应的id值
    for k, v in big_ategory2.items():
        for sub_divt in v['list']:
            title = sub_divt['title']
            id = re.findall(category_pattern, sub_divt['link'])[0]
            # 将分类title和id以键值的形式存放在category_dict字典中，方便后面直接根据title取出对应的id值
            category_dict[title] = [id]
            # 将标题添加到准备好的list中
            user_category_list.append(title)
    return category_dict, user_category_list
    # print(category_list)


# 获取商品的列表（writer为csv的句柄，startpage起始页，endpage结束页，category_id菜单id）
def get_product(writer, startpage, endpage, category_id):
    for i in range(startpage, endpage + 1):
        # 拼接一个完整的url
        url = 'http://list.mogujie.com/search?cKey=15&page=%s&sort=pop&ad=2&fcid=%s' % (i, category_id)
        response = requests.get(url)
        # 获取结果后解析提取数据
        parse(writer, response.text)


def parse(writer, text):
    # 先将数据转换成python对象，然后取出商品列表
    data = json.loads(text)['result']['wall']['docs']
    # 循环遍历
    for item in data:
        # print(item)
        title = item['title']
        price = item['price']
        image = item['img']
        link = item['link']
        print(title, price, image, link)
        cursor.execute(self.insert_sql, title, price, image, link)
        connect.commit()
        connect.close()
        dict = {
            'title': title,
            'price': price,
            'image': image,
            'link': link,
        }
        # 将数据写入csv文件中
        write_data(dict)


def write_data(dict):
    writer.writerow(dict)


if __name__ == '__main__':
    # 创建一个数据库连接
    connect = pymysql.Connect(host='localhost', user='root',password='bc123', database='蘑菇街', port=3306, charset='utf8')
    cursor = connect.cursor()
    insert_sql = "INSERT INTO commodity(title,price,image,link) VALUES(%s,%s,%s,%s)"
    # 创建csv的文件
    csv_file = open('mogujie.csv', 'w')
    filed_name = ('title', 'price', 'image', 'link')
    # 创建csv的句柄
    writer = csv.DictWriter(csv_file, fieldnames=filed_name)
    # 　写入顶部的header
    writer.writeheader()
    # 调用函数，获取分类数据和菜单列表
    category_dict, user_categorys = get_all_category()
    # print(category_dict)
    # print(type(category_dict))
    print('尊敬的用户您可以从以下列表中筛选商品:' + '\n' + str(user_categorys))
    kw = input('输入您要选择的商品分类')
    startpage = int(input('输入起始页：'))
    endpage = int(input('输入结束页：'))
    category_id = category_dict[kw]
    get_product(writer, startpage, endpage, category_id)
