# -*- coding: utf-8 -*-
import scrapy
from jobbole_project.items import JobboleProjectItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # 请求状态
        print(response.status)
        articleList = response.css('#archive .post.floated-thumb')
        for node in articleList:
            item = JobboleProjectItem()
            # extract_first('')表示取列表里面的第一个元素，如果列表里面没有值，那会显示你设置的默认值
            item['coverImage'] = node.css('.post-thumb a img ::attr(src)').extract_first("")
            item['title'] = node.css('.archive-title ::text').extract_first("")
            item['url'] = node.css('.archive-title ::attr(href)').extract_first("")
            item['publishTime'] = node.css('.post-meta p ::text').re('\d+/\d+/\d+')[0]
            item['content'] = node.css('span.excerpt p ::text').extract_first("")
            item['tags'] = ','.join(node.css('.post-meta p a[rel="category tag"] ::text').extract())

            # 将item交给数据管道处理
            yield item

        # # 获取当前页面的其他页码的链接（url）
        # pageUrls = response.css('a.page-numbers ::attr(href)').extract()
        # for url in pageUrls:
        #     yield scrapy.Request(url, callback=self.parse)
