# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#通用爬虫提取到的连接会构建一个Link对象
from scrapy.link import Link
from xiachufang.items import XiachufangCaiPuItem,XiachufangTagItem,XiachufangUserInfoItem

from scrapy_redis.spiders import RedisCrawlSpider
#创建通用爬虫的命令：scrapy genspider -t crawl 爬虫名称　域

# class XcfcrawlspiderSpider(CrawlSpider):
class XcfcrawlspiderSpider(RedisCrawlSpider):
    #爬虫名称
    name = 'xcfCrawlSpider'
    #设置允许爬取的域
    allowed_domains = ['xiachufang.com']
    # #设置起始的url
    # 分布式不需要起始url,
    # start_urls = ['http://www.xiachufang.com/category/']
    # 根据redis_key从redis数据库中获取起始任务
    redis_key = 'xcfCrawlSpider:start_urls'
    # LinkExtractor中的相关参数
    """
    allow = (), :设置正则规则,符合正则表达式的所有url都会被提取,
                如果为空,则提取全部的url连接
    restrict_xpaths = ():使用xpath语法,定位到指定的标签(节点)下,
                        在该标签(节点)下获取我们的url连接
    restrict_css = ()
    """

    rules = (
        #分类列表地址
        # http://www.xiachufang.com/category/40073/
        Rule(
            LinkExtractor(allow=r'.*?/category/\d+/'),
            follow=True,
            process_links='check_category_url'
        ),
        # 菜单详情地址,
        # http://www.xiachufang.com/recipe/1055105/
        Rule(
            LinkExtractor(
                allow=r'.*?/recipe/\d+/',
            ),
            callback='parse_caipu_detail',
            follow=True,
        ),
        #用户信息接口
        #http://www.xiachufang.com/cook/118870772/
        Rule(
            LinkExtractor(
                allow=r'.*?/cook/\d+/'
            ),
            callback='parse_userinfo_detail',
            follow=True,
        )
    )


    # def parse(self): 一定不能出现这个方法,因为crawlSpider使用了这个方法
    def parse_start_url(self, response):
        tags = response.xpath('//div[@class="cates-list-mini clearfix "]/ul/li//a')

        for tag_a in tags:
            tag_href = tag_a.xpath('./@href').extract_first()
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
                tag_item['tagName'] = tag_a.xpath('./text()').extract_first()
                tag_item['firstUrl'] = response.urljoin(tag_href)
                tag_item['uniqueType'] = tag_a.xpath('./@href').re('\d+')[0]

                yield tag_item


    def check_category_url(self,links):
        """
        可以在此方法做对规则提取的url构建成的的link对象做过滤处理
        :param links:
        :return:
        """
        # print('===================',links,'===================')
        return links

    def parse_caipu_detail(self,response):
        """
        菜谱详情请求成功后的结果处理,从响应结果中提取目标数据
        :param response:
        :return:
        """
        print('详情获取成功')
        # print(response.status,response.url)
        # 取出item
        cp_item = XiachufangCaiPuItem()
        #分类
        cp_item['tag'] = response.xpath('//div[@class="page-outer"]/div/ol/li[2]/a/text()').extract_first('')
        # 图片链接
        cp_item['coverImage'] = response.xpath('//div[@class="cover image expandable block-negative-margin"]/img/@src').extract_first('')
        # 名称
        cp_item['title'] = ''.join(response.xpath('//h1[@class="page-title"]/text()').extract()).replace(' ','').replace('\n','')
        # 评分
        cp_item['score'] = response.xpath('//div[@class="score float-left"]/span[@class="number"]/text()').extract_first('')
        # 多少人做过
        cp_item['doitnum'] = response.xpath('//div[@class="cooked float-left"]/span[@class="number"]/text()').extract_first('')
        # 发布人
        cp_item['author'] = response.xpath('//div[@class="author"]/a[1]/span/text()').extract_first('')
        # 获取用料的列表
        # 对吓：8只;对吓：8只;对吓：8只;对吓：8只;对吓：8只
        tr_list = response.css('div.ings tr')
        used_list = []
        for tr in tr_list:
            name = ''.join(tr.css('td.name ::text').extract()).replace('\n', '').replace(' ', '')
            value = ''.join(tr.css('td.unit ::text').extract()).replace('\n', '').replace(' ', '')
            if len(value) == 0:
                value = '若干'
            used_list.append(name + ':' + value)
        cp_item['used'] = ';'.join(used_list)
        # 获取做法
        cp_item['methodway'] = '->'.join(response.css('div.steps p.text ::text').extract())

        yield cp_item

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


