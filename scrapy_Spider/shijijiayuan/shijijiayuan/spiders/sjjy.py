# -*- coding: utf-8 -*-
import scrapy
import json,re
from shijijiayuan.items import ShijijiayuanItem
from w3lib.html import remove_tags
from scrapy.selector import Selector


class SjjySpider(scrapy.Spider):
    name = 'sjjy'
    allowed_domains = ['jiayuan.com']
    start_urls = ['http://search.jiayuan.com/v2/search_v2.php']

    def start_requests(self):
        """

        :return:
        """
        form_data = {
            'sex': 'f',
            'key': '',
            'stc': '1: 41, 2: 20.28, 23: 1',
            'sn': 'default',
            'sv': '1',
            'p': '1',
            'f': 'search',
            'listStyle': 'bigPhoto',
            'pri_uid': '0',
            'jsversion': 'v5'
        }
        # formdata:对应的是表单数据
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,formdata=form_data,dont_filter=True,meta={'form_data':form_data})
    def parse(self, response):
        patter = re.compile('jiayser##(.*?)##jiayser##',re.S)
        result = re.findall(patter,response.text)[0]
        data = json.loads(result)
        for userinfo in data['userInfo']:
            item = ShijijiayuanItem()
            item['Uid'] = userinfo['uid']
            # 头像
            item['HeaderImage'] = userinfo['image']
            # 性别
            item['Sex'] = userinfo['sex']
            # 标签
            item['RandTag'] = remove_tags(userinfo['randTag'])
            # 年龄
            item['Age'] = userinfo['age']
            # 身高
            item['Height'] = userinfo['height']
            # 个性签名
            item['Shortnote'] = userinfo['shortnote']
            # 工作地点
            item['WorkAdress'] = userinfo['work_sublocation']
            # 需求
            item['MatchCtion'] = userinfo['matchCondition']
            # 匿名名称
            item['NickName'] = userinfo['nickname']
            print(item)

        # 发起发一页请求
        form_data = response.meta['form_data']
        cur_page = form_data['p']
        next_page = int(cur_page)+1
        pageTotal = int(data['pageTotal'])

        if next_page < pageTotal:
            form_data['p'] = str(next_page)

            yield scrapy.FormRequest('http://search.jiayuan.com/v2/search_v2.php',formdata=form_data,meta={'form_data':form_data},callback=self.parse)