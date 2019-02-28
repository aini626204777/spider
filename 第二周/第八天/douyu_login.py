from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path='/home/wjj/文档/spider/chromedriver'
)

driver.get('https://passport.douyu.com/member/login')

time.sleep(1)

driver.find_element_by_xpath('//span[@class="scancide-to js-to-link js-need-param fr"]').click()

driver.find_element_by_xpath('//input[@class="fr ipt ipt-need-parent country-phonenum"]').send_keys('18518753265')

driver.find_element_by_xpath('//input[@class="ipt showpw1 notsub"]').send_keys('ljh12345678')

time.sleep(3)

driver.find_element_by_xpath('//input[@class="loginbox-sbt btn-sub"]').click()

time.sleep(2)

div_image = driver.find_element_by_xpath('//div[@class="geetest_panel_box"]')
#
location = div_image.location
size = div_image.size
print(div_image.location)
print(div_image.size)
# {'y': 180, 'x': 869}
# {'width': 262, 'height': 334}
top,bottom,right,left = location['y']+2,location['y']+size['height']-42,location['x']-4,location['x']-size['width']

time.sleep(3)
#获取屏幕截图
from PIL import Image
from io import BytesIO
screen_image = driver.get_screenshot_as_png()
screen_image = Image.open(BytesIO(screen_image))

caption_image = screen_image.crop((left,top,right,bottom))

caption_image.save('caption_image.png')

