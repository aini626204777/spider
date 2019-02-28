import requests
from lxml import etree

cookie_str = """_uab_collina=154096827317555175990353; UM_distinctid=166c8ddd59166-0abf3ff29b1f45-1e2e130c-1fa400-166c8ddd5934c1; zg_did=%7B%22did%22%3A%20%22166c8ddd88a24d-0bf0dbe15e1415-1e2e130c-1fa400-166c8ddd88c51f%22%7D; saveFpTip=true; QCCSESSID=4fsfdre0pg31bh34a38odkikl0; hasShow=1; acw_tc=75a11e2015470319695314183e6de297db7e7bf8311225c97a69fdb94c; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1547032226,1547032499; CNZZDATA1254842228=996490895-1540965260-%7C1547033072; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201547031960556%2C%22updated%22%3A%201547033530457%2C%22info%22%3A%201547031960560%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%224ecca93f3349b65947ff2c6d33503045%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1547033531"""

# print(cookie_str.split('; '))
cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie_str.split('; ')}

headers = {
    'Referer': 'https://www.qichacha.com/g_BJ',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

url = 'https://www.qichacha.com/firm_0d1793ebae6175bc84406f49c43ae446.html'

response = requests.get(url,headers=headers,cookies=cookies)

print(response.status_code)

response = etree.HTML(response.text)

print(response)

# print(response)

def parse_company_detail(response):
    """
    解析公司详情的数据
    :param response: 公司详情的响应结果
    :return:
    """
    print('正在解析公司详情')
    #实例化一个QichachaCompanyItem对象
    # company_item = QichachaCompanyItem()
    # if "企查查" in response.text:
    if response:
        # 公司所属的分类
        # company_item['sign'] = response.meta['sign']
        company_item = {}
        # 公司名称
        company_item['companyName'] = response.xpath('//div[@class="row title jk-tip"]/h1/text()')[0]
        # 是否在业
        company_item['tags'] = ','.join(response.xpath('//div[@class="row tags"]/span/text()'))
        # 电话
        #先做一个判断是否存在电话号码
        if len(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[1]/span[@class="cvlu"]/span')) > 0:
            company_item['phonenum'] = response.xpath('//div[@class="content"]/div[@class="row"][1]/span[1]/span[@class="cvlu"]/span/text()')[0].replace(' ','').replace('\n','')
            # print(len(phonenum))
        else:
            company_item['phonenum'] = '暂无'
            # print(phonenum)
        # 官网
        if len(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a')) > 0:
            company_item['website'] = response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a[1]/text()')[0]
        else:
            company_item['website'] = '暂无'
        # 邮箱
        if len(response.xpath('//div[@class="content"]/div[@class="row"][2]/span[1]/span[@class="cvlu"]/a')) > 0:
            company_item['email'] = response.xpath('//div[@class="content"]/div[@class="row"][2]/span[1]/span[@class="cvlu"]/a/text()')[0].replace(' ','').replace('\n','')
        else:
            company_item['email'] = '暂无'
        # 浏览量
        company_item['watchnum'] = response.xpath('//div[@class="company-record"]/span[1]/text()')[0].replace('浏览：','')
        # # 法人代表
        company_item['lagal'] = response.xpath('//a[@class="bname"]/h2/text()')[0].replace(' ','').replace('\n','')
 
        # 注册资本
        # company_item['capital'] = response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[1]/td[2]/text()')[0].replace(' ','').replace('\n','')
        company_item['capital'] = response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td[2]/text()')[0]

        company_item['build_date'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td[8]/text()'))
        # 统一社会信用代码
        company_item['credit_code'] = ''.join(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]//td[10]/text()')).replace('\n','').replace(' ','')
        print(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr/td'),len(response.xpath('//section[@id="Cominfo"]/table[@class="ntable"][2]/tr/td')))
        # 成立日期
        # company_item['build_date'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[2]/td[4]/text()')).replace('\n','').replace(' ','')
        # # 公司地址
        # company_item['address'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[10]/td[2]/text()')).replace('\n','').replace(' ','')
        # # 统一社会信用代码
        # company_item['credit_code'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[4]/td[4]/text()')).replace('\n','').replace(' ','')
        # # 注册号
        # company_item['regist_number'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[4]/td[2]/text()')).replace('\n','').replace(' ','')
        # # 公司类型
        # company_item['company_type'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[5]/td[2]/text()')).replace('\n','').replace(' ','')
        # # 所属行业
        # company_item['industry'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[5]/td[4]/text()')).replace('\n','').replace(' ', '')
        # # 登记机关
        # company_item['registration_authority'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[6]/td[4]/text()')).replace('\n','').replace(' ', '')
        # # 营业期限
        # company_item['business_term'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[9]/td[4]/text()')).replace('\n','').replace(' ', '')
        # # 人员规模
        # company_item['person_number'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[9]/td[2]/text()')).replace('\n','').replace(' ', '')
        # # 经营范围
        # company_item['scope'] = response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[last()]/td[2]/text()')[0].replace('\n','').replace(' ','')

        #print(company_item)

        print(company_item)

parse_company_detail(response)