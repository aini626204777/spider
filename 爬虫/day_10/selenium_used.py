from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

# 模拟浏览器发起一个请求
browse.get('https://www.baidu.com')

# 获取的是浏览器渲染之后的页面
print(browse.page_source)

# 如何模拟用户输入
browse.find_element_by_id('kw').send_keys('美女')
# 模拟用户点击
time.sleep(3)
# 模拟回车键
browse.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(3)
# # 模拟点击下一页
# browse.find_element_by_class_name('n').click()
# browse.find_element_by_id('kw').clear()
# time.sleep(3)
# browse.find_element_by_id('kw').send_keys('风景')
# time.sleep(3)
# browse.find_element_by_id('su').send_keys(Keys.RETURN)
# time.sleep(3)
# # 保存照片
# browse.save_screenshot('baidu.png')

browse.find_element_by_xpath('//div[@class="s_tab"]/a[last()]').click()

# # 向后退
# browse.back()
# # 向前退
# browse.forward()
time.sleep(3)
# # browse.close()
browse.quit()
