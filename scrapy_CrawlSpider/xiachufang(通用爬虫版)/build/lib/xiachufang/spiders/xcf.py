# -*- coding: utf-8 -*-
import scrapy
from xiachufang.items import XiachufangTagItem,XiachufangCaiPuItem,XiachufangUserInfoItem
from scrapy_redis.spiders import RedisSpider


class XcfSpider(RedisSpider):
    name = 'xcf'
    allowed_domains = ['xiachufang.com']
    #start_urls = ['https://www.xiachufang.com/category/40076/?page=1']
    # start_urls = ['http://www.xiachufang.com/category/']
    redis_key = 'xcf:start_urls'

    def start_requests(self):
        """
        重写这个方法的目的可以根据自己的需求发起请求
        :return:
        """
        for url in self.start_urls:
            # yield scrapy.Request(url,callback=self.parse_category,dont_filter=True)
            yield  scrapy.Request(url,dont_filter=True)

    def parse(self,response):
        """
        获取所有的分类菜单的链接
        :param response:
        :return:
        """
        print(response.status,'分类菜单页面获取完毕')
        tags = response.css('div.cates-list-mini.clearfix ul li a')
        print(tags)
        for tag_a in tags:
            tag_href = tag_a.css('::attr(href)').extract_first()
            if tag_href and 'category' in tag_href:
                """
                #分类名称
                tagName = scrapy.Field()
                #分类首页地址
                firstUrl = scrapy.Field()
                #标识
                uniqueType = scrapy.Field()
                """
                tag_item = XiachufangTagItem()
                tag_item['tagName'] = tag_a.css('::text').extract_first()
                tag_item['firstUrl'] = response.urljoin(tag_href)
                tag_item['uniqueType'] = tag_a.css('::attr(href)').re('\d+')[0]
                yield tag_item
                yield scrapy.Request(tag_item['firstUrl'],callback=self.parse_caidan_list,meta={'tag':tag_item['tagName']})

    def parse_caidan_list(self, response):

        print(response.status)
        tag = response.meta['tag']
        #获取菜谱的列表
        caipu_list = response.css('div.pure-u-3-4.category-recipe-list ul li')
        print(len(caipu_list))
        for caipu_li in caipu_list:
            item = XiachufangCaiPuItem()
            # 分类
            item['tag'] = tag
            # 图片链接
            item['coverImage'] = caipu_li.css('div.cover.pure-u img::attr(data-src)').extract_first('')
            # # 名称
            item['title'] = caipu_li.css('div.info.pure-u > p.name a::text').extract_first('').replace('\n','').replace(' ','')
            #在获取(评分和多少人做过)之前需要判断一下
            spans = caipu_li.css('p.stats > span')
            if len(spans) > 1:
                # # 评分
                item['score'] = spans[0].css('::text').extract_first('')
                # # 多少人做过
                item['doitnum'] = spans[1].css('::text').extract_first('')
            elif len(spans) == 1:
                # # 评分
                item['score'] = '0'
                # # 多少人做过
                item['doitnum'] = spans[0].css('::text').extract_first('')
            elif len(spans) == 0:
                # # 评分
                item['score'] = '0'
                # # 多少人做过
                item['doitnum'] = '0'

            # # 发布人
            item['author'] = caipu_li.css('p.author a')[0].css('::text').extract_first('')

            #获取详情的地址
            detail_url = caipu_li.css('div.info.pure-u > p.name a ::attr(href)').extract_first()

            if detail_url:
                #得到完整的url地址
                detail_url = response.urljoin(detail_url)
                yield scrapy.Request(detail_url,callback=self.parse_detail_data,meta={'item':item})

        #获取下一页地址,如果存在继续发起请求，不存在则不在发起请求
        next_page_url = response.css('div.pager > a.next ::attr(href)').extract_first()
        if next_page_url:
            next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse_caidan_list,meta={'tag':tag})

        # 方式二获取所有的分页url地址,然后发起请求
        # next_pages = response.css('div.pager a ::attr(href)').extract()
        # if len(next_pages) > 0:
        #     for url in next_pages:
        #         next_page_url = response.urljoin(url)
        #         yield scrapy.Request(next_page_url,callback=self.parse_caidan_list,meta={'tag':tag})

    def parse_detail_data(self,response):
        #取出item
        item = response.meta['item']
        #获取用料的列表
        # 对吓：8只;对吓：8只;对吓：8只;对吓：8只;对吓：8只
        tr_list = response.css('div.ings tr')
        used_list = []
        for tr in tr_list:
            name = ''.join(tr.css('td.name ::text').extract()).replace('\n','').replace(' ','')
            value = ''.join(tr.css('td.unit ::text').extract()).replace('\n','').replace(' ','')
            if len(value) == 0:
                value = '若干'
            used_list.append(name+':'+value)
        item['used'] = ';'.join(used_list)
        #获取做法
        item['methodway'] = '->'.join(response.css('div.steps p.text ::text').extract())
        # print(item)
        yield item

        #用户详情链接
        users = response.xpath('//a[@class="avatar-link avatar"]/@href').extract()
        if len(users) > 0:
            for user_url in users:
                user_url = response.urljoin(user_url)
                yield scrapy.Request(user_url,callback=self.parse_userinfo_detail)

    def parse_userinfo_detail(self,response):
        """
        :param response:
        :return:
        """
        import re
        user_item = XiachufangUserInfoItem()
        # 用户名
        user_item['username'] = response.xpath('//h1[@class="page-title mb10"]/text()').extract_first('').replace('\n','').replace(' ','')
        # 用户唯一标识
        user_item['uniqueType'] = re.findall('\d+',response.url)[0]
        # 性别
        user_item['gender'] = response.xpath('//span[@class="mr10 display-inline-block"][1]/text()').extract_first('')
        # 居住地
        adress_elements = response.xpath('//i[@class="icon-profile icon-profile-location"]')
        if len(adress_elements) > 0:
            user_item['adress'] = adress_elements[0].xpath('../text()').extract_first('')
        else:
            user_item['adress'] = ''
        # 加入时间
        user_item['joinTime'] = response.xpath('//span[@class="display-inline-block"]/text()').extract_first('')
        # 关注数
        user_item['attentNum'] = response.xpath('//a[@class="bold font16"][1]//text()').extract_first('')
        # 被关注数
        user_item['fans'] = response.xpath('//a[@class="bold font16"][2]//text()').extract_first('')
        # 菜谱数量
        user_item['cpNum'] = response.xpath('//div[@class="tab-bar pure-g"]/ul/li[2]/a/span/text()').re('\d+')[0]
        # 作品数量
        user_item['zpNum'] = response.xpath('//div[@class="tab-bar pure-g"]/ul/li[3]/a/span/text()').re('\d+')[0]
        # 个人简介
        user_item['info'] = ''.join(response.xpath('//div[@class="people-base-desc dark-gray-font mt10"]//text()').extract()).replace(' ','').replace('\n','').replace('\r','')

        print(user_item)

        yield user_item


