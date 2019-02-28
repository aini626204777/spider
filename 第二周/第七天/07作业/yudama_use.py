from YDMHTTPApi import check_code

from selenium import webdriver
import requests,time

driver = webdriver.Chrome(executable_path='/home/ljh/桌面/driver/chromedriver')

driver.get('https://www.douban.com/')

driver.implicitly_wait(5)

#输入账号
driver.find_element_by_id('form_email').send_keys('18518753265')

#输入密码

driver.find_element_by_id('form_password').send_keys('ljh12345678')

#输入验证码

#获取图片的连接
from selenium.common import exceptions
try:
    code_image_url = driver.find_element_by_id('captcha_image').get_attribute('src')
    print(code_image_url)
    response = requests.get(code_image_url)
    with open('code_image.png','wb') as f:
        f.write(response.content)

    #根据图片识别验证码
    filename = 'code_image.png'
    codetype = '3006'
    result = check_code(filename,codetype)

    print(result)

    #将验证码写入输入框
    driver.find_element_by_id('captcha_field').send_keys(result)
except exceptions.NoSuchElementException as err:
    print(err)

time.sleep(8)

#点击登录按钮
driver.find_element_by_class_name('bn-submit').click()

cookies = driver.get_cookies()
cookies_dict = {i['name']:i['value'] for i in cookies}
print(cookies_dict)



#添加cookies
# driver.add_cookie(cookies_dict)





