# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qidianCrawlSpider.items import QidiancrawlspiderBookItem, QidiancrawlspiderChpaterItem


class QidianSpider(CrawlSpider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1']

    rules = (
        # 如果Rule对象中没有设置callback回调，那么follow默认为True
        # 提取书籍分页
        Rule(LinkExtractor(allow=r'.*?orderId.*?&page=\d+', restrict_xpaths='//ul[@class="lbf-pagination-item-list"]'),
             callback='parse_item', follow=False),

        # 提取书籍详情
        Rule(LinkExtractor(allow=r'.*?/info/\d+', restrict_xpaths='//ul[@class="all-img-list cf"]'),
             process_links='get_book_link', callback='parse_book_detail', follow=True, ),

        # 提取章节详情
        Rule(LinkExtractor(allow=r'.*?//read.qidian.com/chapter/.*?', restrict_xpaths='//div[@class="volume"]/ul[@class="cf"]'),
             callback='parse_chpater_detail', follow=True)
    )

    def parse_start_url(self, response):
        """
        如果想要对起始url的响应结果做处理的话,就需要回调这个方法
        :param response:
        :return:
        """
        self.parse_item(response)

    def parse_item(self, response):
        # print(response.status,response.url)
        books = response.xpath('//ul[@class="all-img-list cf"]/li')

        for book_info in books:
            book_item = QidiancrawlspiderBookItem()
            # 封面图片
            book_item['coverImage'] = response.urljoin(
                book_info.xpath('.//div[@class="book-img-box"]/a/img/@src').extract()[0])
            # 标题
            book_item['bookName'] = book_info.xpath('.//div[@class="book-mid-info"]/h4/a/text()').extract()[0]
            # 作者
            book_item['author'] = book_info.xpath('.//a[@class="name"]/text()').extract()[0]
            # 分类
            book_item['tags'] = '·'.join(book_info.xpath('.//p[@class="author"]/a[position()>1]/text()').extract())
            # 连载状态
            book_item['status'] = book_info.xpath('.//p[@class="author"]/span/text()').extract()[0]
            # 简介
            book_item['content'] = book_info.xpath('.//p[@class="intro"]/text()').extract()[0].split()[0]

    def get_book_link(self, links):
        for link in links:
            link.url = link.url + '#Catalog'

        return links

    def parse_book_detail(self, response):
        """
        获取章节url地址（章节）
        :param response:
        :return:
        """
        # print('获取到了书页详情！！！', response.status, response.url)

        pass
    def parse_chpater_list(self, response):
        import json
        data = json.loads(response.text)
        vs = data['data']['vs']
        for sub_vs in vs:
            if int(sub_vs['vs']) == 0:
                print('免费章节')
                cs = sub_vs['cs']
                for sub_cs in cs:
                    pass

    def parse_chpater_detail(self, response):
        print('获取到了章节详情', response.status, response.url)
        chpater_item = QidiancrawlspiderChpaterItem()
        # 标题
        chpater_item['chpaterName'] = response.xpath('//h3[@class="j_chapterName"]/text()').extract_first('')
        # 数据名称
        chpater_item['bookName'] = response.xpath('//a[@class="act"]/text()').extract_first('')
        # 字数
        chpater_item['fontsize'] = response.xpath('//span[@class="j_chapterWordCut"]/text()').extract_first('')
        # 发布时间
        chpater_item['publishTime'] = response.xpath('//span[@class="j_updateTime"]/text()').extract_first('')
        # 内容
        chpater_item['content'] = ''.join(
            response.xpath('//div[@class="read-content j_readContent"]//text()').extract()).replace(' ', '').replace(
            '\n', '').replace('\u3000', '')
        print(chpater_item)
