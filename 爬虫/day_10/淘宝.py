from selenium import webdriver
import time
from lxml import etree
import pymysql


#设置无头浏览器
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.set_headless()
chrome_options = webdriver.ChromeOptions()
chrome_options.set_headless()

# 一定要注意driver驱动的版本和谷歌浏览器的版本

browser = webdriver.Chrome(executable_path="/home/bc/桌面/chromedriver",options=chrome_options)
# browser = webdriver.PhantomJS(executable_path='/Users/ljh/Desktop/phantomjs')
# browser = webdriver.Firefox(executable_path='/Users/ljh/Desktop/geckodriver')

#搜索美食信息
def search():
    #打开淘宝首页
    browser.get("https://www.taobao.com")
    #等待3秒
    browser.implicitly_wait(3)
    #输入搜索关键子
    browser.find_element_by_class_name("search-combobox-input").send_keys("美食")
    #等待5秒页面加载完毕
    time.sleep(5)
    #找到搜索按钮点击，获取商品列表页面源码
    browser.find_element_by_class_name("btn-search").click()
    if browser.page_source:
        getprodect_items(browser.page_source)


#获取商品列表的数据
def getprodect_items(html):
    response = etree.HTML(html)
    # items = response.xpath("//div[@class='item J_MouserOnverReq ']")
    items = response.xpath("//div[@class='item J_MouserOnverReq  ']")
    print(items)
    for each in items:
        # print(each)
        # print('提取数据，这里自己写')
        image_url = each.xpath('.//img[@class="J_ItemPic img"]/@src')[0]
        price = each.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()')[0]
        store = each.xpath('.//a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[2]/text()')[0]
        buynum = each.xpath('.//div[@class="deal-cnt"]/text()')[0]
        location = each.xpath('.//div[@class="location"]/text()')[0]
        # title = each.xpath('.//a[@class="J_ClickStat"]/text()')[0]

        #image_url、title、buynum、price、store、location
        print("------华丽的商品分割线-----")
        print("商品图片地址："+"https:"+image_url)
        # print("商品名称:"+title)
        print("商品价格:"+price)
        print("购买数量:"+buynum)
        print("商店地址:"+location)
        print("店铺名称:"+store)
        connect = pymysql.connect(host='localhost', user='root', passwd='bc123', database='淘宝美食', port=3306,
                                  charset='utf8')
        cursor = connect.cursor()
        insert_sql = "INSERT INTO meishi2(store,location,buynum,price,image_url) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(insert_sql,(store,location,buynum,price,image_url))
        connect.commit()
        connect.close()
        # 这里需要将数据写如数据库


    # 获取下一页的数据
    # time.sleep(5)
    #找到下一页的按钮，并点击获取下一页商品列表源码
    # browser.find_element_by_css_selector("li.item.next a.J_Ajax.num.icon-tag").click()
    # 如果数据存在就进行提取数据
    # if browser.page_source:
    #     time.sleep(2)
    #     # 递归方法获取数据
    #     getprodect_items(browser.page_source)


def main():
    search()
    # time.sleep(15)
    # 测试时，停留15秒后关闭浏览器
    # browser.quit()

if __name__ == '__main__':

    main()