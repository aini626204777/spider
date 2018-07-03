from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os
drive = webdriver.Chrome(executable_path='/home/run/桌面/chromedriver')
drive.get('https://www.zhaopin.com/')

sr = drive.find_elements_by_xpath(".//*[@id='KeyWord_kw2']")
sr[0].send_keys('技术')
drive.find_element_by_class_name("doSearch").click()

# print(drive.page_source)

soup = BeautifulSoup(drive.page_source)

a = soup.select('.zwmc div a')
list = []
for i in a:
    print(i.get_text())
    dit = {
        '职位':i.get_text()
    }
    list.append(dit)

list = json.dumps(list)
ww = open('json文件.json','w')
ww.write(list)

sr = drive.find_elements_by_xpath(".//*[@id='goto']")
sr[0].send_keys()
drive.find_element_by_class_name("next-page").click()
