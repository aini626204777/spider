# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from fake_useragent import UserAgent
from lxml import etree
from bs4 import BeautifulSoup
import os
import json

dirver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
dirver.get('https://www.zhaopin.com/')
dirver.find_element_by_id('KeyWord_kw2').send_keys('技术')
dirver.find_element_by_class_name('doSearch').click()
ua = UserAgent()

sou = BeautifulSoup(dirver.page_source)

a = sou.select('.zwmc div a')
list = []
for i in a:
    print(i.get_text())
    dit = {
        '职位':i.get_text()
    }
    list.append(dit)
list = json.dumps(list)
with open('json文件.json','w') as w:
    w.write(list)
sr = dirver.find_element_by_xpath(".//*[@id='goto']")
sr[0].send_keys()
dirver.find_element_by_class_name("next-page").click()
