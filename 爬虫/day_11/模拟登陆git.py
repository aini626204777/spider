# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browse = webdriver.Chrome(executable_path='/home/bc/下载/chromedriver')
browse.get('https://github.com/login')
browse.implicitly_wait(5)
try:
    #browse.find_element_by_css_selector('.text-bold.text-white.no-underline').click()
    browse.find_element_by_id('login_field').send_keys('15110500442')
    browse.find_element_by_id('password').send_keys('sjl1314520')
    browse.find_element_by_css_selector('.btn.btn-primary.btn-block').click()
    browse.find_element_by_css_selector('.avatar.float-left.mr-1').click()
    #browse.find_element_by_xpath('//ul[@class="dropdown-menu dropdown-menu-sw"]/li[2]/a').click()
    cookies= browse.get_cookies()
    print(cookies[::-1])
    cookie = ''
    for cookieitem in cookies[::-1]:
        print(cookieitem['name'],cookieitem['value'])
        cookie += cookieitem['name'] + '=' + cookieitem['value'] + ';'
    print(cookie)
    with open('githubcookie.txt', 'w') as f:
       f.write(cookie[:-2])

except NoSuchElementException:
    print('')

# with open('github.html','w') as f:
#     f.write(browse.page_source)
