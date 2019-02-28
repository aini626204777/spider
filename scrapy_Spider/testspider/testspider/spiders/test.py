# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    # name是爬虫名称
    name = 'test'
    # allowed_domains设置允许爬取的域(可以指定多个)
    allowed_domains = ['baidu.com']
    # start_urls设置其实url，可以设置多个
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        """
        是一个回调方法，起始url请求成功后，会自动回调这个方法
        :param response: 响应结果
        :return:
        """
        # 请求的状态码
        code = response.status
        print(code)
        # 获取响应的页面源码
        html = response.text
        with open('baidu.html','w') as f:
            f.write(html)

        # 获取响应页面的二进制数据
        b_html = response.body
        print('b_html==',b_html)
        # 获取响应头
        response_headers = response.headers
        print('response_headers==',response_headers)
        # 获取当前请求的url地址
        current_url = response.url
        print('current_url==',current_url)
        # 获取当前请求的request对象
        request = response.request
        print('request==',request)
        # 获取请求的请求头
        headers = request.headers
        print('headers==',headers)
        pass
