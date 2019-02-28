import requests, re, pymysql
from fake_useragent import UserAgent


class ZhilianSpider(object):
    def __init__(self):
        self.url = 'https://fe-api.zhaopin.com/c/i/sou?'
        self.parmars = {
            'start': 0,
            'pageSize': 90,
            'cityId': 530,
            'workExperience': -1,
            'education': -1,
            'companyType': -1,
            'employmentType': -1,
            'jobWelfareTag': -1,
            'kw': 'python',
            'kt': 3,
        }
        self.req_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

    def load_page_data(self, url, parmars, headers):
        response = requests.get(url=url, params=parmars, headers=headers)
        if response.status_code == 200:
            jobs = response.json()['data']['results']
            for jobinfo in jobs:
                jobdata = {}
                jobdata['jobName'] = jobinfo['jobName']
                jobdata['salary'] = jobinfo['salary']
                jobdata['display'] = jobinfo['city']['display']
                jobdata['workingExp'] = jobinfo['workingExp']['name']
                jobdata['eduLevel'] = jobinfo['eduLevel']['name']
                jobdata['welfare'] = ','.join(jobinfo['welfare'])
                jobdata['company'] = jobinfo['company']['name']
                jobdata['type'] = jobinfo['company']['type']['name']
                jobdata['size'] = jobinfo['company']['size']['name']

                # self.save_data_to_db('zhilian',jobdata)

                # 公司详情目标url
                number = jobinfo['company']['number']
                company_url = 'https://company.zhaopin.com/' + number + '.htm'
                resufl = self.load_company_data(company_url)
                if resufl.status_code == 200:
                    pattern = re.compile(
                        'detail-info__title__txt">(.*?)</h1>.*?main__number__content">(.*?)</span>.*?main__number__content">(.*?)</span>.*?main__number__content">(.*?)</span>.*?company-show__content__description">(.*?)<!---->',
                        re.S)
                    data = re.findall(pattern, resufl.text)
                    for i in data:
                        company_data = {}
                        company_data['company_name'] = i[0]
                        company_data['company_type'] = i[1]
                        company_data['company_number'] = i[2]
                        company_data['company_business'] = i[3]
                        company_data['company_introduction'] = i[4]
                        # self.save_data_to_db('ZL_company_data', company_data)
            numFound = response.json()['data']['numFound']
            if self.parmars['start'] < int(numFound):
                self.parmars['start'] = int(self.parmars['start']) + 90
                self.load_page_data(self.url, self.parmars, self.req_headers)

    def load_company_data(self, company_url):
        response = requests.get(url=company_url, headers=self.req_headers)
        if response.status_code == 200:
            return response

    def save_data_to_db(self, table, jobdata):
        connect = pymysql.Connect('localhost', "root", "abcd1234", "1712B", 3306, charset="utf8")
        keys = ','.join(jobdata.keys())
        sql = """INSERT INTO {table}({columns}) values ({values})""".format(table=table, columns=keys,
                                                                            values=(','.join(["%s"] * len(jobdata))))
        cr = connect.cursor()
        cr.execute(sql, list(jobdata.values()))
        connect.commit()
        cr.close()
        connect.close()


if __name__ == '__main__':
    zhilian = ZhilianSpider()
    zhilian.load_page_data(zhilian.url, zhilian.parmars, zhilian.req_headers)
