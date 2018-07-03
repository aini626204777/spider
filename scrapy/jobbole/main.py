import os,sys
# 程序的执行模块
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy','crawl','Jobbole'])