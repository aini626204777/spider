# -*- coding: utf-8 -*-

# Scrapy settings for tianyancha_and_qichacha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tianyancha_and_qichacha'

SPIDER_MODULES = ['tianyancha_and_qichacha.spiders']
NEWSPIDER_MODULE = 'tianyancha_and_qichacha.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'tianyancha_and_qichacha (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tianyancha_and_qichacha.middlewares.TianyanchaAndQichachaSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tianyancha_and_qichacha.middlewares.CookiesDownLoadMiddlerware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'tianyancha_and_qichacha.pipelines.TianyanchaAndQichachaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 企查查
# cookie = {'UM_distinctid': '168354618ba17f-0d936c03ccb199-18211c0a-1fa400-168354618bb280;',
#           ' zg_did': '%7B%22did%22%3A%20%2216835461c7732b-0b5d87de19ad7b-18211c0a-1fa400-16835461c781cf%22%7D; ',
#           'hasShow': '1; ',
#           '_uab_collina': '154708201525587956439935',
#           'saveFpTip': 'true; ',
#           'acw_tc': '2aec23d015470820382481345e4c4dee172eb9f9a080407e12d21b8c48;',
#           'QCCSESSID': 'a2isle7s2mentqimd700u8smp2; ',
#           'zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f': '%7B%22sid%22%3A%201547097831760%2C%22updated%22%3A%201547103722981%2C%22info%22%3A%201547082013838%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22e770bfcdfb43e09ea61868e47d040db0%22%7D;',
#           'CNZZDATA1254842228': '217812370-1547081099-https%253A%252F%252Fwww.google.com%252F%7C1547102807;',
#           'Hm_lvt_3456bee468c83cc63fb5147f119f1075': '1547082189,1547087923,1547097833,1547103724;',
#           'Hm_lpvt_3456bee468c83cc63fb5147f119f1075': '1547103724'}

# 天眼查
# COOKIES = ['TYCID=3cb59b00147311e9b1435f5679084138; undefined=3cb59b00147311e9b1435f5679084138; ssuid=3683521903; _ga=GA1.2.1527400986.1547082089; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E7%25BB%25B4%25E6%258B%2589%25C2%25B7%25E6%25B3%2595%25E7%25B1%25B3%25E5%258A%25A0%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzE0MDY2OTYyMyIsImlhdCI6MTU0NzEwOTYzMSwiZXhwIjoxNTYyNjYxNjMxfQ.C9p0pj-j9tEhIrwbZ8FZt6qS_4h7xB_EBNQCLcNqicZWmTplnlL4essXpjxUUByj8NjRBZdoZR8Fr03fDajp1g%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213140669623%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzE0MDY2OTYyMyIsImlhdCI6MTU0NzEwOTYzMSwiZXhwIjoxNTYyNjYxNjMxfQ.C9p0pj-j9tEhIrwbZ8FZt6qS_4h7xB_EBNQCLcNqicZWmTplnlL4essXpjxUUByj8NjRBZdoZR8Fr03fDajp1g; aliyungf_tc=AQAAAMooy1UJnQgApJOePXiIIeLzMM+R; csrfToken=5z1RN3YPJ5F_Gn0bhJmEYDLh; __insp_wid=677961980; __insp_slim=1547382482066; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vc2VhcmNoP2Jhc2U9Ymomcm5kPQ%3D%3D; __insp_targlpt=5YyX5Lqs5biC5YWs5Y_45L_h5oGv5p_l6K_iX_S8geS4muW3peWVhuS%2FoeaBr1%2FljJfkuqzluILkvIHkuJrkv6HnlKjkv6Hmga%2Fmn6Xor6LlubPlj7At5aSp55y85p_l; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1547082089,1547083016,1547109492,1547382485; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1547382485; _gid=GA1.2.421253171.1547382485; _gat_gtag_UA_123487620_1=1; __insp_norec_sess=true']

# ＭｙＳＱＬ链接数据库信息
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = 'abcd1234'
MYSQL_DB = 'xiaoxiangmu'
MYSQL_CHARSET = 'utf8'
