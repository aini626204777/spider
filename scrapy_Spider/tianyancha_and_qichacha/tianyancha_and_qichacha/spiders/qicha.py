# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tianyancha_and_qichacha.items import QichachaCompanyItem,QichachaClassfyItem


class QichaSpider(CrawlSpider):
    name = 'qicha'
    allowed_domains = ['qichacha.com']
    start_urls = ['https://www.qichacha.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/g.*?', restrict_xpaths='//ul[@class="sidebar-hangye-list"]/li'),
             callback='parse_page_data', follow=True),
        Rule(LinkExtractor(allow=r'com/firm.*?', restrict_xpaths='//div[@class="row"]/div[2]/section'),
             callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        """
        分类的信息
        :param response:
        :return:
        """
        ul_list = response.xpath('//ul[@class="sidebar-hangye-list"]/li')
        # 分类的字段
        for li in ul_list:

            item = QichachaClassfyItem()
            # 哪个网站
            item["fromdomains"] = response.xpath('//img[@class="m-r-sm"]/@alt').extract()[0]
            # 分类名称
            item["classifyName"] = li.xpath('.//a/text()').extract_first('')
            # 分类的表示
            item["sign"] = li.xpath('.//a/@href').extract()[0]
            # 首页列表地址
            item["firstUrl"] = 'https://www.qichacha.com'+li.xpath('.//a/@href').extract_first('')

            yield item

    def parse_page(self, response):
        pass

    def parse_company_detail(self, response):
        """
        解析公司详情的数据
        :param response: 公司详情的响应结果
        :return:
        """
        print('正在解析公司详情', response.status, response.url)
        # 实例化一个QichachaCompanyItem对象
        company_item = QichachaCompanyItem()
        if "企查查" in response.text:

            # 公司所属的分类
            company_item['classifyName'] = response.meta['sign']
            # 哪个网站
            company_item['fromdomains'] = '企查查'
            # 公司名称
            company_item['companyName'] = response.xpath('//div[@class="row title jk-tip"]/h1/text()').extract_first(
                '暂无')
            # 是否在业
            company_item['tags'] = ','.join(response.xpath('//div[@class="row tags"]/span/text()').extract())
            # 电话
            # 先做一个判断是否存在电话号码
            if len(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[1]/span[@class="cvlu"]/span')) > 0:
                company_item['phonenum'] = response.xpath(
                    '//div[@class="content"]/div[@class="row"][1]/span[1]/span[@class="cvlu"]/span/text()').extract_first(
                    '').replace(' ', '').replace('\n', '')
                # print(len(phonenum))
            else:
                company_item['phonenum'] = '暂无'
                # print(phonenum)
            # 官网
            if len(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a')) > 0:
                company_item['website'] = response.xpath(
                    '//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a[1]/text()').extract_first('')
            else:
                company_item['website'] = '暂无'
            # 邮箱
            if len(response.xpath('//div[@class="content"]/div[@class="row"][2]/span[1]/span[@class="cvlu"]/a')) > 0:
                company_item['email'] = response.xpath(
                    '//div[@class="content"]/div[@class="row"][2]/span[1]/span[@class="cvlu"]/a/text()').extract_first(
                    '').replace(' ', '').replace('\n', '')
            else:
                company_item['email'] = '暂无'
            # 　浏览量
            company_item['watchnum'] = response.xpath('//div[@class="company-record"]/span[1]/text()').extract_first(
                '').replace('浏览：', '')
            # 　更新日期
            company_item['updateTime'] = ''.join(
                response.xpath('//div[@class="company-action"]/p[@class="m-t"]/text()').extract()).replace('\n',
                                                                                                           '').replace(
                ' ', '')

            if len(response.xpath('//a[@class="bname"]/h2')) > 0:

                # 法人代表
                company_item['lagal'] = response.xpath('//a[@class="bname"]/h2/text()').extract_first('').replace(' ',
                                                                                                                  '').replace(
                    '\n', '')
                # 注册资本（无）
                company_item['capital'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    1].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 实交资本（无）
                company_item['relcapital'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    3].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 经营状态
                company_item['scopeStatus'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    5].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 成立日期
                company_item['buildDate'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    7].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 统一社会信用代码
                company_item['creditCode'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    9].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 　纳税人识别号
                company_item['ratepayerCode'] = \
                response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[11].xpath(
                    './/text()').extract_first('').replace('\n', '').replace(' ', '')
                # 注册号
                company_item['registNumber'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    13].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 组织机构代码
                company_item['institutionalNumber'] = \
                response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[15].xpath(
                    './/text()').extract_first('').replace('\n', '').replace(' ', '')
                # 公司类型
                company_item['companyType'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    17].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 所属行业
                company_item['industry'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    19].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 核准日期
                company_item['checkTime'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    21].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 登记机关
                company_item['registration_authority'] = \
                response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[23].xpath(
                    './/text()').extract_first('').replace('\n', '').replace(' ', '')
                # 所属地
                company_item['place_origin'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    25].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 英文名
                company_item['englishName'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    27].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 曾用名
                company_item['oldName'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    29].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 参保人数
                company_item['insuredNumber'] = \
                response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[31].xpath(
                    './/text()').extract_first('').replace('\n', '').replace(' ', '')
                if '-' in company_item['insuredNumber']:
                    company_item['insuredNumber'] = 0
                else:
                    company_item['insuredNumber'] = int(company_item['insuredNumber'])
                # 人员规模
                company_item['person_number'] = \
                response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[33].xpath(
                    './/text()').extract_first('').replace('\n', '').replace(' ', '')
                # 营业期限
                company_item['business_term'] = \
                response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[35].xpath(
                    './/text()').extract_first('').replace('\n', '').replace(' ', '')
                # 公司地址
                company_item['address'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    37].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
                # 经营范围
                company_item['scope'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td')[
                    39].xpath('.//text()').extract_first('').replace('\n', '').replace(' ', '')
            else:

                # with open('otherpage.html','w') as file:
                #     file.write(response.text)
                # 公司名称
                company_item['companyName'] = response.xpath('//div[@class="row title"]/text()').extract_first('暂无')
                # 是否在业
                company_item['tags'] = ','.join(response.xpath('//div[@class="row tags"]//text()').extract())
                # 统一社会信用代码
                company_item['creditCode'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[1]/td[2]/text()').extract())
                # 法人代表
                company_item['lagal'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[2]/td[2]/text()').extract())
                # 注册资本（无）
                company_item['capital'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[2]/td[4]/text()').extract())
                # 实交资本（无）
                company_item['relcapital'] = '暂无'
                # 成立日期
                company_item['buildDate'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[3]/td[2]/text()').extract())
                # 经营状态
                company_item['scopeStatus'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[3]/td[4]/text()').extract())
                # 　纳税人识别号
                company_item['ratepayerCode'] = '暂无'
                # 注册号
                company_item['registNumber'] = '暂无'
                # 组织机构代码
                company_item['institutionalNumber'] = '暂无'
                # 公司类型
                company_item['companyType'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[4]/td[2]/text()').extract())
                # 登记机关
                company_item['registration_authority'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[4]/td[4]/text()').extract())
                # 所属行业
                company_item['industry'] = '暂无'
                # 核准日期
                company_item['checkTime'] = '暂无'
                # 所属地
                company_item['place_origin'] = '暂无'
                # 英文名
                company_item['englishName'] = '暂无'
                # 曾用名
                company_item['oldName'] = '暂无'
                # 参保人数
                company_item['insuredNumber'] = 0
                # 人员规模
                company_item['person_number'] = '暂无'
                # 营业期限
                company_item['business_term'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[5]/td[4]/text()').extract())
                # 经营范围
                company_item['scope'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[5]/td[2]/text()').extract())
                # 公司地址
                company_item['address'] = self.deal_with_str(
                    response.xpath('//section[@id="Cominfo"]/table[@class="ntable"]/tr[6]/td[2]/text()').extract())

            # print(company_item)

            yield company_item

        else:
            # with open('detailpage.html','w') as file:
            #     file.write(response.text)
            print('企查查详情数据获取失败', response.url)

    def deal_with_str(self, dataarr):

        str = ''.join(dataarr).replace('\n', '').replace(' ', '')

        return str

