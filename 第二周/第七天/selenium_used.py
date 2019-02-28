#　selenium:是一个web的自动化测试工具,可以直接运行在浏览器上,
# 但是并不自带浏览器,需要有浏览器驱动,selenium可以根据我们的代码指令
# 让浏览器自动加载页面,这时得到的页面源码是经过浏览器渲染之后的,
# 然后我们就可以在页面源码中寻找节点(动态加载的网页,模拟登录)

#pip3 install selenium
from selenium import webdriver

#加载页面
# driver = webdriver.Firefox(
#     executable_path='/home/ljh/桌面/driver/geckodriver'
# )
# #使用get方法打开页面
# driver.get('https://www.baidu.com/')

#加载页面(PhantomJS,无头浏览器)
#warnings.warn('Selenium support for PhantomJS
# has been deprecated, please use headless '
#目前推荐使用谷歌的屋头浏览器
# driver = webdriver.PhantomJS(
#     executable_path='/home/ljh/桌面/driver/phantomjs'
# )
# driver.get('https://www.baidu.com/')
#
# driver.save_screenshot('baidu.png')

# 加载页面(使用谷歌的浏览器驱动)
driver = webdriver.Chrome(
    executable_path='/home/wjj/文档/spider/chromedriver'
)
#设置页面的加载时间
driver.set_page_load_timeout(10)

#导入容错的模块
from selenium.common import exceptions
try:
    driver.get('https://www.baidu.com/')
except exceptions.TimeoutException as err:
    print(err,'请求超时')

#可以获得信息
# 获取页面源码(经过浏览器渲染之后的)
page_html = driver.page_source
with open('baidu.html','w') as file:
    file.write(page_html)
#获取cookies信息
"""
[
{'domain': 
'.baidu.com', 
'httpOnly': False, 
'path': '/', 
'secure': False, 
'value': '1431_21080_28206_28131_27750_28139_27509', 
'name': 'H_PS_PSSID'}, 
{'domain': '.baidu.com', 'httpOnly': False, 'path': '/', 'expiry': 3693275324.184597, 'secure': False, 'value': '8C1C72599F01E693A201BA4B33C6DFE0', 'name': 'BIDUPSID'}, {'domain': '.baidu.com', 'httpOnly': False, 'path': '/', 'secure': False, 'value': '0', 'name': 'delPer'}, {'domain': '.baidu.com', 'httpOnly': False, 'path': '/', 'expiry': 3693275324.184649, 'secure': False, 'value': '1545791676', 'name': 'PSTM'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'path': '/', 'expiry': 1546655678, 'secure': False, 'value': '123353', 'name': 'BD_UPN'}, {'domain': 'www.baidu.com', 'httpOnly': False, 'path': '/', 'secure': False, 'value': '0', 'name': 'BD_HOME'}, {'domain': '.baidu.com', 'httpOnly': False, 'path': '/', 'expiry': 3693275324.18448, 'secure': False, 'value': '8C1C72599F01E693A201BA4B33C6DFE0:FG=1', 'name': 'BAIDUID'}]

"""
#获取所有的cookies值
cookies = driver.get_cookies()
#获取某一个cookies值
driver.get_cookie('BD_UPN')
cookies_dict = {cookie['name']:cookie['value'] for cookie in cookies}
print(cookies)
print(cookies_dict)



#关闭操作
#关闭当前所在的窗口
driver.close()
#退出浏览器
driver.quit()



