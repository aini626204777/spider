# -*- coding: utf-8 -*-
import scrapy
from qichacha.items import QichachaCompanyItem,QichachaClassfyItem
import re,random

class TianyanSpider(scrapy.Spider):
    name = 'tianyan'
    allowed_domains = ['tianyancha.com']
    start_urls = ['https://www.tianyancha.com/']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            'qichacha.middlewares.ProxyMiddleware': 543,
        }
    }

    def parse(self, response):
        """
        解析出天眼查所有的区域分类信息
        :param response:
        :return:
        """
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

            # print(classify_item)

            yield classify_item

            cookie_str = random.choice(self.settings['TYC_COOKIES'])
            cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie_str.split('; ')}
            headers = {
                'Referer': 'https://www.tianyancha.com/',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            }

            yield scrapy.Request(
                classify_item['firstUrl'],
                callback=self.parse_company_list,
                cookies = cookies,
                headers = headers,
                meta={
                    'classifyName':classify_item['classifyName'],
                    'sign':classify_item['sign'],
                }
            )

    def parse_company_list(self,response):
        """
        获取公司详情地址，发起请求,
        获取其他分页地址，发起请求
        :param response:
        :return:
        """
        company_list = response.xpath('//div[@class="search-item sv-search-company"]')
        if len(company_list) > 0:
            print('列表数据获取成功', len(company_list))
            for div_tag in company_list:
                # 提取标题
                title = div_tag.xpath('.//a[@class="name "]/text()').extract_first('').replace(' ', '')
                # 提取公司详情的连接
                detail_url = div_tag.xpath('.//a[@class="name "]/@href').extract_first('')

                # print('正在发起' + title + '请求', detail_url)
                yield scrapy.Request(
                    detail_url,
                    callback=self.parse_company_detail,
                    meta=response.meta,
                )

            # 这里最好是一页一页的提取：
            next_page = response.xpath(
                '//a[@class="num -next"]/@href').extract_first()
            if next_page:
                next_page = response.urljoin(next_page)
                print('正在发起下一页请求：' + next_page)
                yield scrapy.Request(next_page, callback=self.parse_company_list, meta={'sign': response.meta['sign']})
            else:
                print('没有获取到下一页')

            # step2.获取当前页面中其他分页地址(获取当前页面中的其他分页地址)
            other_page = response.xpath('//ul[@class="pagination"]/li/a/@href').extract()
            if len(other_page) > 0:
                for pageurl in other_page:
                    pageUrl = response.urljoin(pageurl)
                    yield scrapy.Request(pageUrl, callback=self.parse_company_list,meta={'sign': response.meta['sign']})
        else:
            print('列表数据获取失败', len(company_list))
            yield scrapy.Request(response.url, callback=self.parse_company_list, meta={'sign': response.meta['sign']})

    def parse_company_detail(self,response):
        print('详情数据获取成功',response.status,response.url)

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

