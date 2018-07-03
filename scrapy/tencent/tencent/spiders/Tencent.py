# -*- coding: utf-8 -*-
import scrapy
import re
from tencent.items import TencentItem
from urllib.parse import urljoin


# 它负处理所有Responses
class TencentSpider(scrapy.Spider):
    # 爬虫的名称，启动爬虫的时候会根据名称找对应的爬虫文件
    name = 'Tencent'
    # 允许爬取的域名，你要爬取的链接必须在这个域下,可以是多个
    allowed_domains = ['hr.tencent.com']
    # 起始url　，可以是多个
    start_urls = ['https://hr.tencent.com/position.php']
    base_url = 'https://hr.tencent.com/position.php'

    # 解析数据在这个,response返回请求的结果
    def parse(self, response):
        print(response.status)
        # 是一个二进制文件
        # print(response.body)
        # pass

        job_even = response.xpath('//tr[@class="even"]/td[@class="l square"]/a/@href').extract()
        job_odd = response.xpath('//tr[@class="odd"]/td[@class="l square"]/a/@href').extract()
        # print(job_even,job_odd)
        jobs = job_odd + job_even
        # print(jobs)
        for nodeurl in jobs:
            fullurl = urljoin('https://hr.tencent.com/position.php', nodeurl)
            print(fullurl)

            # yield在这里是相当于实现了异步，每当余姚yield就会先暂停一下
            # 然后先返回yield后面的值，下次在执行的时候，会从上次的执行中断的地方开始
            yield scrapy.Request(fullurl, callback=self.parseJobDetail)
        links = response.xpath('//div[@class="pagenav"]//a/@href').extract()
        for url in links:
            if 'position.php' in url:
                print(url)
                fullurl = urljoin(self.base_url,url)
                yield scrapy.Request(fullurl,callback=self.parse)

    def parseJobDetail(self, response):
        tiems = TencentItem()
        tiems['jobName'] = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
        tiems['workLocation'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        tiems['jobType'] = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
        tiems['jobDesc'] = response.xpath('//table[@class="tablelist textl"]/tr[3]/td/ul/li/text()').extract()
        tiems['jobInfo'] = response.xpath('//table[@class="tablelist textl"]/tr[4]/td/ul/li/text()').extract()
        yield tiems
