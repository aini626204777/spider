from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import requests
from YDMHTTPApi import check_code


# opt = webdriver.ChromeOptions()
# opt.set_headless()
driver = webdriver.Chrome(executable_path='/home/wjj/文档/spider/chromedriver')

# driver.set_page_load_timeout(10)

def download_img():
    driver.get('https://www.douban.com/accounts/login?source=main')
    driver.find_element_by_id('email').send_keys('626204777@qq.com')
    driver.find_element_by_id('password').send_keys('wangjunjie521')
    driver.find_element_by_class_name('btn-submit').click()
    # driver.get('https://www.douban.com/accounts/login?source=main')
    # driver.find_element_by_id('email').send_keys('626204777')
    result = load_img()
    denglu(filename=result)




def load_img():
    xpath = '//*[@id="captcha_image"]'
    href = driver.find_element_by_xpath(xpath).get_attribute('src')
    data = requests.get(href)
    print(href)
    with open('yanzhengma.jpg', 'wb') as file:
        file.write(data.content)
    filename = "yanzhengma.jpg"
    codeType = 3007
    result = check_code(filename, codeType)
    return result

def denglu(filename):
    # driver.find_element_by_id('email').send_keys('626204777')
    driver.find_element_by_id('password').send_keys('wangjunjie521')
    driver.find_element_by_id('captcha_field').send_keys(filename)
    driver.find_element_by_class_name('btn-submit').click()
    driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[4]/ul/li[3]/a').click()
    parse_data()


def parse_data():
    window = driver.window_handles
    driver.switch_to.window(window[-1])

    driver.find_element_by_id('inp-query').send_keys('成龙')
    driver.find_element_by_class_name('inp-btn').click()
if __name__ == '__main__':
    download_img()


