# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class DownloadmiddlerwareSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DownloadmiddlerwareDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentDownloadMiddlerware(object):

    # def __init__(self,User_Agents):
    #     self.User_agents = User_Agents
    #
    # @classmethod
    # def from_crawler(cls,crawler):
    #     User_Agents = crawler.settings['USERAGENT']
    #
    #     return cls(User_Agents)

    def process_request(self,request,spider):
        """
        所有的request在交给下载器之前,都会经过这个方法
        :param request:
        :param spider:
        :return:
        """
        import random
        # random_ua = random.choice(self.User_agents)


        # User_Agent = spider.settings['USERAGENT']
        # random_ua = random.choice(User_Agent)

        from fake_useragent import UserAgent
        userAgent = UserAgent()
        random_ua = userAgent.random

        if random_ua:
            print('经过了下载中间件',random_ua)
            request.headers['User-Agent'] = random_ua
            # request.headers.setdefault(b'User-Agent',random_ua)

class ProxyDownloadMiddlerware(object):

    def process_request(self,request,spider):
        proxies = spider.settings['PROXIES']
        import random
        proxy_rm = random.choice(proxies)

        if proxy_rm['pwd']:
            #只有账号密码的代理
            #对账号密码进行base64编码
            import base64
            base64_pwd = base64.b64encode(proxy_rm['pwd'].encode('utf-8')).decode('utf-8')
            #对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_pwd
            #设置ip
            request.meta['proxy'] = proxy_rm['ip']
        else:
            # 设置ip
            request.meta['proxy'] = proxy_rm['ip']

class CookiesDownLoadMiddlerware(object):

    def process_request(self,request,spider):

        COOKIES = spider.settings['COOKIES']
        import random
        cookie_rm = random.choice(COOKIES)
        if cookie_rm:
            request.cookies = cookie_rm

#scrapy并不支持动态加载网页的爬取
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
class SeleniumDownloadMiddlerWare(object):

    # def __init__(self):
    #     #创建浏览器驱动
    #     self.driver = webdriver.Chrome(
    #         executable_path=''
    #     )
    #     self.driver.set_page_load_timeout(10)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.

        s = cls()
        #使用信号量,监控爬虫结束的信号
        crawler.signals.connect(s.close, signal=signals.spider_closed)
        return s

    def close(self, spider):
        import time
        time.sleep(5)
        spider.driver.close()

    def process_request(self,request,spider):
        if spider.name == 'test':
            #获取url
            url = request.url

            if url:
                try:
                    # self.driver.get(url)
                    spider.driver.get(url)
                    # pageSource = self.driver.page_source
                    pageSource = spider.driver.page_source

                    if pageSource:
                        """
                        url, status=200, headers=None, 
                        body=b'', flags=None, request=None
                        """
                        return HtmlResponse(
                            url=url,
                            status=200,
                            body=pageSource.encode('utf-8'),
                            request=request
                        )

                except TimeoutException as err:
                    print('请求超时',url)
                    return HtmlResponse(
                        url=url,
                        status=408,
                        body=b'',
                        request=request
                    )




