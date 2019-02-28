# -*- coding: utf-8 -*-

# Scrapy settings for qichacha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qichacha'

SPIDER_MODULES = ['qichacha.spiders']
NEWSPIDER_MODULE = 'qichacha.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qichacha (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'cookie': 'acw_tc=3c1cb09c15409682667032696e3977cfe9d753635f42e0ac99999fc67d; _uab_collina=154096827317555175990353; UM_distinctid=166c8ddd59166-0abf3ff29b1f45-1e2e130c-1fa400-166c8ddd5934c1; zg_did=%7B%22did%22%3A%20%22166c8ddd88a24d-0bf0dbe15e1415-1e2e130c-1fa400-166c8ddd88c51f%22%7D; saveFpTip=true; hasShow=1; QCCSESSID=99d7n7icj47t7ct4da2qo6g9g1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1543373115,1543379776,1543390133,1543408672; CNZZDATA1254842228=996490895-1540965260-%7C1543411797; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201543405913055%2C%22updated%22%3A%201543411831920%2C%22info%22%3A%201543112422850%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%224ecca93f3349b65947ff2c6d33503045%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1543411833',
    # 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qichacha.middlewares.QichachaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'qichacha.middlewares.ProxyMiddleware': 543,
# #    # 'qichacha.middlewares.QichachaProxyDownloaderMiddleware':543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#激活管道
ITEM_PIPELINES = {
   'qichacha.pipelines.QichachaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#数据库信息配置
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PWD = 'ljh1314'
MYSQL_DB = 'companydb'
MYSQL_CHARSET = 'utf8'

QCC_COOKIES = [
    "UM_distinctid=1675a485dd34cb-061770d063e28e-74266752-1fa400-1675a485dd4495; CNZZDATA1254842228=676282574-1543406397-null%7C1547091041; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1547033721,1547049552,1547096340; zg_did=%7B%22did%22%3A%20%221675a485ede13b-0fa3b735c13cd28-74266752-1fa400-1675a485edf442%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201547096324795%2C%22updated%22%3A%201547096397452%2C%22info%22%3A%201547033721112%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%221baec61a358ce5cc6ab6d1db66813162%22%7D; _uab_collina=154340795559081848997662; saveFpTip=true; acw_tc=75a11e2515470337194435592e490513381d8700ad03732a208d67c7d1; QCCSESSID=vcr80fe414co3tss32v6njq431; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1547096397",
    "UM_distinctid=1675a485dd34cb-061770d063e28e-74266752-1fa400-1675a485dd4495; CNZZDATA1254842228=676282574-1543406397-null%7C1547047452; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1547033721,1547049552; zg_did=%7B%22did%22%3A%20%221675a485ede13b-0fa3b735c13cd28-74266752-1fa400-1675a485edf442%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201547049551660%2C%22updated%22%3A%201547049601139%2C%22info%22%3A%201547033721112%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%22165cd9d39bfebaf22e1b4786b168646f%22%7D; _uab_collina=154340795559081848997662; saveFpTip=true; acw_tc=75a11e2515470337194435592e490513381d8700ad03732a208d67c7d1; QCCSESSID=vcr80fe414co3tss32v6njq431; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1547049600; hasShow=1",
    "acw_tc=75a11e1c15471198031866392e74550e5ea0c378f76f1be7c0b5fd24e4; QCCSESSID=kbnljis77s6ukgvhgvvpqm3b37; zg_did=%7B%22did%22%3A%20%221683786bf31389-008ec9d84d6759-3c720356-1fa400-1683786bf321fb%22%7D; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201547119804213%2C%22updated%22%3A%201547119804213%2C%22info%22%3A%201547119804224%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%7D; UM_distinctid=1683786c05d1d1-0bef5985841278-3c720356-1fa400-1683786c05e26a; CNZZDATA1254842228=2064655457-1547119795-%7C1547119795; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1547119805; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1547119805; _uab_collina=154711980717752063461223; saveFpTip=true"
]

TYC_COOKIES = [
    "TYCID=0bdcf1b0ddad11e8b4498ff5c7376b63; undefined=0bdcf1b0ddad11e8b4498ff5c7376b63; ssuid=2395190752; _ga=GA1.2.998069065.1541059609; aliyungf_tc=AQAAAIQgPlzG1wgASUxI34HTj6HaCHin; csrfToken=F9Jk0Y2rTgclZk9urzWW0gUk; _gid=GA1.2.305538714.1547042104; RTYCID=50082525023a4e75a90c550fe9bf241c; CT_TYCID=ca433ec9d666444f976427eda45d8d98; token=4465a54a540740128447b85046618923; _utm=2ba113b4db9f4bd699834a1a247af4d1; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E7%25BB%25B4%25E6%258B%2589%25C2%25B7%25E6%25B3%2595%25E7%25B1%25B3%25E5%258A%25A0%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUxODc1MzI2NSIsImlhdCI6MTU0NzA3NjE0OSwiZXhwIjoxNTYyNjI4MTQ5fQ.6XWBdNUdVqF2XnCfc1MwP5xRH_WOx2VwqiQyWSYUHr3iHzQkS0DRQgaDG5coRJYsNmZs2GMlCWqVx5SdzlZBSQ%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218518753265%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODUxODc1MzI2NSIsImlhdCI6MTU0NzA3NjE0OSwiZXhwIjoxNTYyNjI4MTQ5fQ.6XWBdNUdVqF2XnCfc1MwP5xRH_WOx2VwqiQyWSYUHr3iHzQkS0DRQgaDG5coRJYsNmZs2GMlCWqVx5SdzlZBSQ; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1546861423,1547042104,1547075252,1547088076; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY29tcGFueS84ODAwNzc5OQ%3D%3D; __insp_targlpt=5rC45a6J5L_h77yI5aSp5rSl77yJ6IKh5p2D5oqV6LWE5Z_66YeR566h55CG5pyJ6ZmQ5YWs5Y_4X_W3peWVhuS%2FoeaBr1%2Fkv6HnlKjmiqXlkYpf6LSi5Yqh5oql6KGoX_eUteivneWcsOWdgOafpeivoi3lpKnnnLzmn6U%3D; cloud_token=7fc936651cb74ae188e0fbe8e4c7e00f; cloud_utm=6a78b7cfa94045fa82b873c47b1ebbc4; __insp_norec_sess=true; _gat_gtag_UA_123487620_1=1; __insp_slim=1547097155280; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1547097157",
    "aliyungf_tc=AQAAAFds4Fx8CQsAsRJAfMdULCe8Kk9W; csrfToken=tWNHV7gjhSlEhTbLRn-cJsCZ; TYCID=77737b4014af11e984c64bd75932259d; undefined=77737b4014af11e984c64bd75932259d; ssuid=8992763118; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v; __insp_targlpt=5aSp55y85p_lLeS6uuS6uumDveWcqOeUqOWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fmn6Xor6Lns7vnu58%3D; __insp_norec_sess=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1547107966; _ga=GA1.2.1377580664.1547107968; _gid=GA1.2.1415494900.1547107968; token=f620165cf4ff4d25b9e02872aa0a3fe1; _utm=e4f638942aaf4d958f3387ba861a56a1; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%2596%2587%25C2%25B7%25E8%25BF%25AA%25E5%25A1%259E%25E5%25B0%2594%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzAzNDAyMDc2MSIsImlhdCI6MTU0NzEwOTA2NiwiZXhwIjoxNTYyNjYxMDY2fQ.CCef6uLX38lb2nwBCZGMtHXzJdasJOiXAk92NdIlkxo1qorENXkxwJUTcvhiYDu9_wUvxPrUmwLK6HG7hmI57Q%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217034020761%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzAzNDAyMDc2MSIsImlhdCI6MTU0NzEwOTA2NiwiZXhwIjoxNTYyNjYxMDY2fQ.CCef6uLX38lb2nwBCZGMtHXzJdasJOiXAk92NdIlkxo1qorENXkxwJUTcvhiYDu9_wUvxPrUmwLK6HG7hmI57Q; _gat_gtag_UA_123487620_1=1; __insp_slim=1547109082529; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1547109094; RTYCID=90ca45fa9b574572a77824ebed40ffa6",
    "aliyungf_tc=AQAAABvQMkF6yAcA8RFAfD4F74NN4GnX; csrfToken=5hynqnvdMpvVIjxEFdeMlcrs; RTYCID=c88274d65e924ad29442bf54a7e46057; CT_TYCID=1118f47b66b04e849b3ddb8307652c2f; ssuid=557966617; TYCID=b6958fe014b211e9b8996745efeceb78; undefined=b6958fe014b211e9b8996745efeceb78; token=2f4a8b6ac85b4175bcdff2c988530db6; _utm=82343cfdd8704b52a689d8fa8b1c29bf; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E6%2596%2587%25C2%25B7%25E8%25BF%25AA%25E5%25A1%259E%25E5%25B0%2594%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTk3Mzg5MzMzNCIsImlhdCI6MTU0NzEwOTQxNiwiZXhwIjoxNTYyNjYxNDE2fQ.ILEDee3up61YQHc97Ag4R2wS_SyJ5ctf725Q8AkZChN-X2aSgGvma_iqkbqeHluCAixgG9Ol6nXowDSHmbGMmw%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215973893334%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTk3Mzg5MzMzNCIsImlhdCI6MTU0NzEwOTQxNiwiZXhwIjoxNTYyNjYxNDE2fQ.ILEDee3up61YQHc97Ag4R2wS_SyJ5ctf725Q8AkZChN-X2aSgGvma_iqkbqeHluCAixgG9Ol6nXowDSHmbGMmw; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vY29tcGFueS8yMDg5MjE4NjA%3D; __insp_targlpt=5aSn5ZCM5biC5Lq65rCR5pS%2F5bqc5Zu95pyJ6LWE5Lqn55uR552j566h55CG5aeU5ZGY5LyaX_W3peWVhuS%2FoeaBr1%2Fkv6HnlKjmiqXlkYpf6LSi5Yqh5oql6KGoX_eUteivneWcsOWdgOafpeivoi3lpKnnnLzmn6U%3D; __insp_norec_sess=true; __insp_slim=1547109430483; _ga=GA1.2.1334063285.1547109431; _gid=GA1.2.417679416.1547109431; _gat_gtag_UA_123487620_1=1; cloud_token=06febc04e48b4d6e8020a41182651cd4; cloud_utm=44807178edc74d57a791df3e5ab41dbc; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1547107966; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1547109434"
]
