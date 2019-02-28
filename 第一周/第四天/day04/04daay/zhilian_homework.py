"""
爬虫的流程：
1.分析网站,获取目标url,发起请求
https://fe-api.zhaopin.com/c/i/sou?
start=0&pageSize=90&cityId=530&workExperience=-1
&education=-1&companyType=-1
&employmentType=-1&jobWelfareTag=-1
&kw=python&kt=3

https://fe-api.zhaopin.com/c/i/sou?
start=90&pageSize=90&cityId=530&workExperience=-1
&education=-1&companyType=-1
&employmentType=-1&jobWelfareTag=-1
&kw=python&kt=3

https://fe-api.zhaopin.com/c/i/sou?
start=180&pageSize=90&cityId=530&workExperience=-1
&education=-1&companyType=-1
&employmentType=-1&jobWelfareTag=-1
&kw=python&kt=3

2.得到数据

3.提取数据

4.保存

"""

import requests
import pymysql
import re
from w3lib.html import remove_tags

class ZhilianSpider(object):

    def __init__(self):
        #职位列表url地址
        self.start_url = 'https://fe-api.zhaopin.com/c/i/sou?'
        #get氢气后拼接的参数
        self.parmars = {
            'start':0,
            'pageSize':90,
            'cityId':530,
            'workExperience':-1,
            'education': -1,
            'companyType': -1,
            'employmentType':-1,
            'jobWelfareTag': -1,
            'kw': 'python',
            'kt': 3,
        }
        #请求头
        self.req_headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

        self.mysql_client = pymysql.Connect(
            '127.0.0.1','root','ljh1314',
            '1712B',3306,charset='utf8'
        )
        self.cursor = self.mysql_client.cursor()

    def load_page_data(self,url,parmars,headers):
        """
        发起请求，获取职位列表数据
        :param url:发起请求的url地址
        :param parmars:get请求拼接的参数(dict)
        :param headers:请求头(dict)
        :return:
        """
        #发起请求
        response = requests.get(url,params=parmars,headers=headers)
        #请求成功,获取职位列表数据
        if response.status_code == 200:
            print(response.json())
            #取出职位信息
            jobs = response.json()['data']['results']
            for job in jobs:
                jobData = {}
                #标题
                jobData['title'] = job['jobName']
                #薪资
                jobData['salary'] = job['salary']

                self.save_data_to_db(jobData,'jobinfo')

                #https://company.zhaopin.com/CZ323676910.htm
                #CZ435840920
                #http://special.zhaopin.com/bj/2010/ghgj121622/index.htm
                #取出公司的唯一标示
                number = job['company']['number']
                #根据唯一标示构造公司详情url地址
                company_url = 'https://company.zhaopin.com/'+number+'.htm'
                #发起请求,获取公司信息
                company_info = self.load_company_data(company_url)
                if company_info:
                                self.save_data_to_db(company_info, 'companyinfo')

            #构建下一页请求(当前页数据获取完毕,发起下一页请求)
            self.parmars['start'] = self.parmars['start'] + 90
            #获取职位总数
            totalnum = int(response.json()['data']['numFound'])
            if self.parmars['start'] < totalnum:
                self.load_page_data(self.start_url,self.parmars,self.req_headers)
            else:
                print('数据获取完毕了')
                self.mysql_client.close()
                self.cursor.close()

    def load_company_data(self,url):
        """
        根据公司详情地址,获取公司详情信息
        :param url:
        :return:
        """
        response = requests.get(url,headers=self.req_headers)

        if response.status_code == 200:
            #正则匹配公司详情数据
            pattern = re.compile(
                '<div.*?background:url\((.*?)\)'+
                '.*?<h1.*?>(.*?)</h1>'+
                '.*?<span.*?main__number__content.*?>(.*?)</span>'+
                '.*?<span.*?main__number__content.*?>(.*?)</span>'+
                '.*?<span.*?main__number__content.*?>(.*?)</span>'+
                '.*?<div\sclass="company-show__content__description">(.*?)</div>',re.S
            )
            info = re.findall(pattern,response.text)
            [('info1','inf2')]
            if len(info) > 0:
                #取出正则匹配到的公司信息
                info = info[0]
                company = {}
                company['coverImage'] = info[0]
                company['title'] = info[1]
                company['type'] = info[2]
                company['model'] = info[3]
                company['info'] = info[4]
                #　提取公司详情数据的时候，可能会有一些标签在详情的div下
                # remove_tags:该方法可以去掉html标签,只留下标签的文本内容
                company['content'] = remove_tags(info[5])
                return company
            else:
                #没有配到数据则返回None
                return None

    def save_data_to_db(self,data,table):
        """
        数据持久化
        :param data: 要存储的数据(字典)
        :param table: 表名
        :return:
        """
        #数据库插入语句
        sql = """
        INSERT INTO %s (%s)
        VALUES (%s)
        """ % (table,','.join(data.keys()),','.join(['%s']*len(data)))
        print(data)
        # try:
        #     #执行数据库语句
        #     self.cursor.execute(sql,list(data.values()))
        #     #提交
        #     self.mysql_client.commit()
        # except Exception as err:
        #     #回滚
        #     self.mysql_client.rollback()
        #     print(err)


if __name__ == '__main__':

    zlSpider = ZhilianSpider()

    zlSpider.load_page_data(zlSpider.start_url,zlSpider.parmars,zlSpider.req_headers)
