# -*- coding:utf-8 -*-
#　可以帮我们随机获取User-Agent
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.chrome)
print(ua.ie)