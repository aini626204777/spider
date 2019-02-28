# from selenium import webdriver
# import time
#
#
#
# driver = webdriver.Chrome(
#     executable_path='/home/wjj/文档/spider/chromedriver'
# )
# driver.get('https://www.zhihu.com/signup?next=%2F')
#
# time.sleep(2)
#
# driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span').click()
#
# time.sleep(1)
# driver.find_element_by_xpath('//div[@class="SignFlow-accountInput Input-wrapper"]/input').send_keys('13140669623')
# driver.find_element_by_xpath('//div[@class="Input-wrapper"]/input').send_keys('mima0321')
# driver.find_element_by_xpath('//button[@class="Button SignFlow-submitButton Button--primary Button--blue"]').click()
#
#
# from selenium.common import exceptions
#
# try:
#     img_element = driver.find_element_by_xpath('//img[@class="Captcha-englishImg"]')
#     if img_element:
#         print('英文验证码')
#
# except exceptions.NoSuchElementException as err:
#     print('倒立验证码')
#     img_element2 = driver.find_element_by_xpath('//img[@class="Captcha-chineseImg"]')
#     # img_data = img_element2.
#
#     import base64
#
#     # image_data_t = base64.b64decode(img_data)
#     # with open('Captcha-chineseImg.gif','w') as f:
#     #     f.write(img_data)

from .zheye import zheye
z = zheye()
positions = z.Recognize('path/to/captcha.gif')


