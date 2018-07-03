from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
from lxml import etree


class toabaoselenium(object):
    def __init__(self):
        self.browse = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')
        self.browse.get('https://www.taobao.com/')
        self.browse.find_element_by_class_name('search-combobox-input').send_keys('食品')
        time.sleep(2)
        self.browse.find_element_by_class_name('btn-search').click()
        html = self.browse.page_source
        self.main(html)

    def main(self, html):
        response = etree.HTML(html)
        # print(response)
        # time.sleep(2)
        if self.browse.page_source:
            shipin_list = response.xpath('//div[@class="items"]')
            for i in shipin_list:
                shop_name = i.xpath('.//a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[2]/text()')
                image = i.xpath('.//img[@class="J_ItemPic img"]/@src')
                price = i.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()')
                client = i.xpath('.//div[@class="deal-cnt"]/text()')
                introduce = i.xpath('.//a[@class="J_ClickStat"]/text()')
                print(shop_name,image,price,client,introduce)
                # dict = {
                #     'shop_name':shop_name,
                #     'image':image,
                #     'price':price,
                #     'client':client,
                #     'introduce':introduce,
                # }
                # print(dict)


if __name__ == '__main__':
    me = toabaoselenium()
