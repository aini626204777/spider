# -*- coding: utf-8 -*-
import scrapy
from jobbole.items import JobboleItem

class JobboleSpider(scrapy.Spider):
    name = 'Jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        urls = response.xpath('//div[@class="post floated-thumb"]/div/a/@href').extract()
        # print(urls)
        for i in urls:
            url = i
            print(i)
            yield scrapy.Request(url,callback=self.parse_content)


    def parse_content(self,response):
        print('开始匹配')
        item = JobboleItem()
        # 标题
        item['title'] = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # 创建时间
        item['create_data'] = response.xpath('//div[@class="entry-meta"]/p/text()').extract()[0]
        # 文章地址
        item['url'] = response.url
        # 图片链接地址
        item['img_url'] = response.xpath('//img[@class="aligncenter"][1]/@src').extract_first('')
        # # 点赞数
        item['praise_nums'] = response.xpath('//div[@class="post-adds"]/span[1]/h10/text()').extract()[0]
        # print(praise_nums)
        # 收藏数量
        item['bookmark_nums'] = response.xpath('//span[@class=" btn-bluet-bigger href-style bookmark-btn  register-user-only "]/text()').extract_first('0')[0]
        # 评论数量
        item['comment_nums'] = response.xpath('//div[@class="post-adds"]/a/span/h10/text()').extract_first('0')[0]
        # 文章内容
        item['content'] =response.xpath('//div[@class="entry"]//p/text()').extract()
        # print(content)
        # # 标签
        item['tags'] =response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        yield item