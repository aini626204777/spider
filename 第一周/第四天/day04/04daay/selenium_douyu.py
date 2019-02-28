from selenium import webdriver
import time
import requests
from io import BytesIO
from PIL import Image
from chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='/home/ljh/桌面/driver/chromedriver')

driver.get('https://passport.douyu.com/member/login?lang=cn&type=login&client_id=1')

driver.find_element_by_xpath('//span[@class="scancide-to js-to-link js-need-param fr"]').click()

driver.find_element_by_name('phoneNum').send_keys('18518753265')

driver.find_element_by_name('password').send_keys('ljh12345678')

time.sleep(1)

driver.find_element_by_xpath('//input[@class="loginbox-sbt btn-sub"]').click()

time.sleep(2)

imgae_element = driver.find_element_by_xpath('//img[@class="geetest_item_img"]')

image_path = imgae_element.get_attribute('src')

location = imgae_element.location

print(location)


# response = requests.get(image_path)
#
# with open('caption.png','wb') as file:
#
#     file.write(response.content)

size = imgae_element.size

print(size)

response = requests.get(image_path)

top,bottom,left,right = location['y']-40,location['y']+size['height'],location['x']-size['width']-30,location['x']

print(top,bottom,left,right)

screen_image = driver.get_screenshot_as_png()

screen_image = Image.open(BytesIO(screen_image))

captcha = screen_image.crop((left,top,right,bottom))

# with open('caption.jpg','wb') as file:
#
#     file.write(response.content)

captcha.save('image.png')

chaojiying = Chaojiying_Client('18518753265', 'ljh12345678', '898122')
im = open('image.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)

pic_str = result['pic_str'].split("|")
locations = [[location for location in pic_location.split(",")] for pic_location in pic_str]
print(locations)

for location in locations:
    ActionChains(driver).move_to_element_with_offset(imgae_element,int(location[0]),int(location[1])-40).click().perform()
    time.sleep(1)


driver.find_element_by_xpath('//div[@class="geetest_commit_tip"]').click()

time.sleep(4)


# print(driver.get_cookies())


