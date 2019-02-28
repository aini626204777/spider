# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tianyancha_and_qichacha.items import QichachaClassfyItem,QichachaCompanyItem
import re

class TianyanSpider(CrawlSpider):
    name = 'tianyan'
    allowed_domains = ['tianyancha.com']
    start_urls = ['https://www.tianyancha.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*?com/search.*?',restrict_xpaths='//div[@class="right -scroll js-industry-container"]'), callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=r'.*?com/search.*?',
                           restrict_xpaths='//div[@class="right -scroll js-industry-container"]'),
             callback='parse_page', follow=True),
    )

    def parse_start_url(self, response):
        '''
        分类信息
        :param response:
        :return:
        '''

        classfies = response.xpath('//div[@class="right -scroll js-industry-container"]//a')

        for a in classfies[0:1]:
            # 分类的item
            classify_item = QichachaClassfyItem()
            # 哪个网站
            classify_item['fromdomains'] = '天眼查'
            # 标题
            classify_item['classifyName'] = a.xpath('./text()').extract_first('')
            # 首页列表地址
            classify_item['firstUrl'] = a.xpath('./@href').extract_first('')
            # 分类id
            classify_item['sign'] = classify_item['firstUrl'].split('=')[1]

            yield classify_item
    def parse_page(self,response):
        print(response.status, response.url)
        pass
    def parse_item(self, response):

        if '天眼查' in response.text:

            company_item = QichachaCompanyItem()
            # 公司所属的分类
            company_item['classifyName'] = response.meta['sign']
            # with open('tycdetail.html','w') as file:
            #     file.write(response.text)
            # # 哪个网站
            company_item['fromdomains'] = '天眼查'
            # # 公司名称
            company_item['companyName'] = response.xpath('//h1[@class="name"]/text()').extract_first('')
            # # 是否在业
            company_item['tags'] = ','.join(response.xpath('//div[@class="tag-list-content"]/div[@class="tag-list"]//text()').extract())
            # # 电话
            company_item['phonenum'] = response.xpath('//div[@class="box -company-box "]//div[@class="detail "]//div[@class="in-block"][1]/span[2]/text()').extract_first('')
            # # 邮箱
            company_item['email'] = response.xpath('//div[@class="box -company-box "]//div[@class="detail "]//div[@class="in-block"][2]/span[@class="email"]/text()').extract_first('')
            # # 官网
            company_item['website'] = response.xpath('//a[@class="company-link"]/text()').extract_first('')
            # # 　浏览量
            company_item['watchnum'] = response.xpath('//span[@class="pv-txt"][2]/text()').extract_first('')
            # # 　更新日期
            company_item['updateTime'] = response.xpath('//span[@class="updatetimeComBox"]/text()').extract_first('')
            # # 法人代表
            company_item['lagal'] = response.xpath('//div[@class="humancompany"]//a[@class="link-click"]/text()').extract_first('')
            # # 注册资本
            company_item['capital'] = response.xpath('//table[@class="table"]//tr[1]/td[2]/div[2]/@title').extract_first('')
            # # 成立日期
            #"pubDate":"1993-11-17T00:00:00","upDate"
            company_item['buildDate'] = re.findall('.*?"pubDate":"(.*?)"',response.text)
            if len(company_item['buildDate']) > 0:
                company_item['buildDate'] =   company_item['buildDate'][0]
            else:
                company_item['buildDate'] = '暂无'
            # 经营状态
            company_item['scopeStatus'] = response.xpath('//table[@class="table"]//tr[3]//div[@class="num-opening"]/text()').extract_first('')
            # 注册号
            company_item['registNumber'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[1]/td[2]/text()').extract_first('')
            # 组织机构代码
            company_item['institutionalNumber'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[1]/td[4]/text()').extract_first('')
            # 统一社会信用代码
            company_item['creditCode'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[2]/td[2]/text()').extract_first('')
            # 公司类型
            company_item['companyType'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[2]/td[4]/text()').extract_first('')
            # 纳税人识别号
            company_item['ratepayerCode'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[3]/td[2]/text()').extract_first('')
            # 所属行业
            company_item['industry'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[3]/td[4]/text()').extract_first('')
            # 营业期限
            company_item['business_term'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[4]/td[2]/span/text()').extract_first('')
            # 核准日期
            company_item['checkTime'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[4]/td[4]/text/text()').extract_first('')
            # 人员规模
            company_item['person_number'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[5]/td[4]/text()').extract_first('')
            # 实缴资本
            company_item['relcapital'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[6]/td[2]/text()').extract_first('')
            # 登记机关
            company_item['registration_authority'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[6]/td[4]/text()').extract_first('')
            # 所属地
            company_item['place_origin'] = '暂无'
            # 曾用名
            company_item['oldName'] = company_item['companyName']
            # # 英文名
            company_item['englishName'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[7]/td[4]/text()').extract_first('')
            # 参保人数
            company_item['insuredNumber'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[7]/td[2]/text()').extract_first('')
            if '-' in company_item['insuredNumber']:
                company_item['insuredNumber'] = 0
            else:
                company_item['insuredNumber'] = int(company_item['insuredNumber'])

            # 公司地址
            company_item['address'] = response.xpath('//table[@class="table -striped-col -border-top-none"]/tbody/tr[8]/td[2]/text()').extract_first('')
            # 经营范围
            company_item['scope'] = ''.join(response.xpath('//span[@class="js-full-container hidden"]/text()').extract()).replace(' ','').replace('\n','').replace('\u3000','')

            yield company_item

        else:
            # with open('detailpage.html','w') as file:
            #     file.write(response.text)
            print('天眼查详情数据获取失败',response.url)
