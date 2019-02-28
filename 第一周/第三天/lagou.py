from urllib import request, parse
from fake_useragent import UserAgent
import json,pymysql,time


def lagouspider(url, formdata, headers):
    """

    :param url: 目标url
    :param formdata: 表单参数
    :param headers: 请求头
    :return:
    """
    formdata = parse.urlencode(formdata).encode('Utf-8')
    req = request.Request(url, headers=headers, data=formdata)
    response = request.urlopen(req)
    result = response.read().decode('Utf-8')
    return result


def load_page_data(url, formdata, headers):
    response = lagouspider(url, formdata, headers)
    data = json.loads(response)
    if data["success"] == True:
        print("请求成功")
        postionJobs = data["content"]["positionResult"]["result"]
        for jobinfo in postionJobs:
            jobdata = {}
            jobdata["positionName"] = jobinfo["positionName"]
            jobdata["formatCreateTime"] = jobinfo["formatCreateTime"]
            jobdata["companyShortName"] = jobinfo["companyShortName"]
            jobdata["salary"] = jobinfo["salary"]
            jobdata["positionAdvantage"] = jobinfo["positionAdvantage"]
            jobdata["workYear"] = jobinfo["workYear"]
            jobdata["education"] = jobinfo["education"]
            jobdata["industryField"] = jobinfo["industryField"]
            jobdata["financeStage"] = jobinfo["financeStage"]
            jobdata["companySize"] = jobinfo["companySize"]
            jobdata["companyLabelList"] = ','.join(jobinfo["companyLabelList"])
            save_data_to_DB(jobdata)


        # 当前页面
        cur_page = int(data["content"]["pageNo"])
        # 每页数据数量
        page_size = data["content"]["pageSize"]
        # 数据总量
        totalcount = data["content"]["positionResult"]["totalCount"]

        if cur_page*int(page_size) < int(totalcount):
            print('数据不够，继续请求！！！')
            next_page = cur_page+1
            formdata['pn'] = next_page
            # 回掉函数
            load_page_data(url,formdata,headers)
    else:
        print('请求不成功,休息一会儿继续请求!!!')
        time.sleep(10)
        print('重新发起第'+str(formdata['pn']+"页请求"))
        lagouspider(url,formdata,headers)

def save_data_to_DB(jobdata):
    """

    :param jobdata: 存储的数据
    :return:
    """
    connect = pymysql.Connect('127.0.0.1', "root", "abcd1234", "1712B", 3306, charset="utf8")
    keys = ','.join(jobdata.keys())
    sql = """INSERT INTO lagou({columns}) values ({values})""".format(columns=keys,values=(','.join(["%s"]*len(jobdata))))
    cr = connect.cursor()
    cr.execute(sql,list(jobdata.values()))
    connect.commit()
    cr.close()
    connect.close()

if __name__ == '__main__':
    '''
    mysql> create table lagou(id int auto_increment primary key,
    -> positionName varchar(225) not null,
    -> formatCreateTime varchar(125),
    -> companyShortName varchar(225),
    -> salary char(225),
    -> positionAdvantage varchar(225),
    -> workYear varchar(220),
    -> education varchar(222),
    -> industryField varchar(222),
    -> financeStage varchar(222),
    -> companySize varchar(222),
    -> companyLabelList varchar(222));
Query OK, 0 rows affected (0.30 sec)

    '''


    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    formdata = {
        'first': 'true',
        'pn': 1,
        'kd': 'c++',
    }
    headers = {'User-Agent': UserAgent().chrome}
    load_page_data(url, formdata, headers)
