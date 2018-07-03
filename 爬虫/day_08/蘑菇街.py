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
    # 首先获取大分类的id
    respoonse = requests.get(
        'http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery2110055639624415818045_1528697742318&pids=110119&_=1528697742319')
    # print(respoonse.text)
    # 创建一个正则对象，去匹配返回结果的json字符串
    pattern = re.compile(r"jQuery.*?\((.*?)\)")
    # 匹配出json字符串
    json_data = re.findall(pattern, respoonse.text)[0]
    print(json_data)
    # 根据json.loads将json字符串转换成python对象
    data = json.loads(json_data)
    # 打印转换后的参数类型
    print(type(data))
    # 取大分类的分类列表
    big_ategory = data['data']['110119']['list']
    # print(big_ategory)
    # 打印分类列表的长度
    print(len(big_ategory))
    # 创建一个list，来放大分类的id
    pids = []
    for item in big_ategory:
        # 将categoryPid加入pids
        pids.append(item['categoryPid'])
    # 将pids的以逗号分割拼接成一个字符串
    pids = ','.join(pids)
    # 打印拼接好的字符串
    print(pids)

    # 根据pids字段来获取全部分类
    url = 'http://mce.mogucdn.com/jsonp/multiget/3'
    # callback=jQuery2110055639624415818045_1528697742318
    # &pids=109499,109520,109731,109753,110549,109779,110548,110547,109757,109793,109795,110563,110546,110544&_=1528697742322
    # 设置get请求的参数
    parmas = {
        'callback': 'jQuery2110055639624415818045_1528697742318',
        'pids': pids,
        '_': '1528697742322',
    }
    # 发起请求获得响应
    response = requests.get(url, params=parmas)
    # print(response.text)
    # 匹配出响应中json字符串，json字符串是所有分类的结果
    all_category_json = re.findall(pattern, response.text)[0]
    # print(all_category_json)
    # 使用json.loads方法将json字符串，转换为python对象
    all_category_data = json.loads(all_category_json)
    # 打印转换后的对象类型
    print(type(all_category_data))
    # print(all_category_data)
    # 获取所有分类的数据信心
    all_category_dict = all_category_data['data']
    # 创建一个正则对象，匹配分类连接的id
    category_pattern = re.compile(r'http.*?/(\d+).*?acm', re.S)
    # 创建category_dict来存放数据，category_dict为字典类型数据
    category_dict = {}
    # 创建user_categorys来存放菜单栏列表，user_categorys为list
    user_categorys = []
    # for循环遍历将菜单的标题和id取出，
    # title放入user_categorys后面将这个列表展示给用户，形成一个菜单栏
    # 将分类title和id以键值的形式存放在category_dict字典中，方便后面直接根据title取出对应的id值
    for k, v in all_category_dict.items():
        # print(k)
        for sub_dict in v['list']:
            title = sub_dict['title']
            id = re.findall(category_pattern, sub_dict['link'])
            # 将分类title和id以键值的形式存放在category_dict字典中，方便后面直接根据title取出对应的id值
            category_dict[title] = id[0]
            # title放入user_categorys后面将这个列表展示给用户，形成一个菜单栏
            user_categorys.append(title)
    # 返回的参数category_dict，和user_categorys
    return category_dict, user_categorys


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
    # 循环遍历，
    for item in data:
        print(item)
        title = item['title']
        price = item['price']
        image = item['img']
        link = item['link']
        print(title, price, image, link)
        # cursor.execute(self.insert_sql,(title,price,image,link))
        # connect.commit()
        # cursor.close()
        dict = {
            'title': title,
            'price': price,
            'image': image,
            'link': link,
        }

        # 将数据写入csv文件
        write_data(dict)


# 保存数据的方法
def write_data(dict):
    writer.writerow(dict)


if __name__ == '__main__':
    # 数据库相关
    # connect = pymysql.Connect('localhost','root','ljh123456','mogujie',3306,charset='utf8')
    # cursor = connect.cursor()
    # insert_sql = """
    # INSERT INTO product(title,price,image,link) VALUES(%s,%s,%s,%s)
    # """
    # 创建csv的文件
    csv_file = open('mogujie.csv', 'a')
    filed_name = ('title', 'price', 'image', 'link')
    # 创建csv的句柄
    writer = csv.DictWriter(csv_file, fieldnames=filed_name)
    # 写入顶部的header
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
    # 获取商品列表数据
    get_product(writer, startpage, endpage, category_id)
