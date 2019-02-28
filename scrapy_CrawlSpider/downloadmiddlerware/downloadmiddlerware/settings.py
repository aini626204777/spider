# -*- coding: utf-8 -*-

# Scrapy settings for downloadmiddlerware project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 项目名称
BOT_NAME = 'downloadmiddlerware'
# 爬虫存储的文件路径
SPIDER_MODULES = ['downloadmiddlerware.spiders']
# 创建爬虫文件的模版,创建好的爬虫文件会存放在这个目录下
NEWSPIDER_MODULE = 'downloadmiddlerware.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 设置ua，来模拟浏览器请求
#USER_AGENT = 'downloadmiddlerware (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 设置是否遵守robot协议,默认为True：遵守
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 设置请求的最大并发数据（下载器）默认是16个
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置请求的下载延时默认为0：没有延时
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 设置网站的最大并发请求数量，默认是8
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 设置某个ip的最大并发请求数量，默认为０
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否携带cookie:默认为true
COOKIES_ENABLED = False

# cookies
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'downloadmiddlerware.middlewares.DownloadmiddlerwareSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'downloadmiddlerware.middlewares.DownloadmiddlerwareDownloaderMiddleware': 543,
   #  'downloadmiddlerware.middlewares.UserAgentDownloadMiddlerware':543,
    'downloadmiddlerware.middlewares.SeleniumDownloadMiddlerWare':543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'downloadmiddlerware.pipelines.DownloadmiddlerwarePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延时默认５秒
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 最大下载延时
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# 针对于网站的最大的并行请求数量
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 调试模式：默认为false,未开启
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 设置数据的缓存，默认情况下是未开启的
#HTTPCACHE_ENABLED = True
# 设置缓存的超市时间，默认为0表示永久有效
#HTTPCACHE_EXPIRATION_SECS = 0
# 设置缓存的存储文件路径
#HTTPCACHE_DIR = 'httpcache'
# 忽略某些状态码的请求结果
#HTTPCACHE_IGNORE_HTTP_CODES = []
# 开启缓存的扩展插件
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USERAGENT = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
]


PROXIES = [
    {'ip':'127.0.0.1:6379','pwd':'ljh:123456'},
    {'ip':'127.0.0.1:6379','pwd':None},
    {'ip':'127.0.0.1:6379','pwd':None},
    {'ip':'127.0.0.1:6379','pwd':None},
    {'ip':'127.0.0.1:6379','pwd':None},
]

#cookies池

COOKIES = [
    {'cookie1':'xxxxxx'},
    {'cookie1':'xxxxxx'},
    {'cookie1':'xxxxxx'},
    {'cookie1':'xxxxxx'},
]
