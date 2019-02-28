# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    # 创建浏览器驱动
    driver = webdriver.Chrome(
        executable_path='/home/ljh/桌面/driver/chromedriver'
    )
    driver.set_page_load_timeout(10)

    def parse(self, response):

        print(response.status,response.request.headers)
