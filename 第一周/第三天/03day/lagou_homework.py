#

#目标url:
# https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false

# post请求要提交的表单数据
# first: true
# pn: 1　（页码）
# kd: c++　(关键字)
from urllib import request,parse
import json,pymysql,time
#pip3 install pymysql


def lagouspider(url,formdata):
    #发起请求返回响应结果
    response_data = load_page_data(url,formdata)
    #得到的数据是一个json字符串,需要转为python类型的数据
    data = json.loads(response_data)
    print(data)

    if data['success']:
        print('请求成功')
        #拿到职位信息
        postionJobs = data['content']['positionResult']['result']
        for jobinfo in postionJobs:
            jobdata = {}
            #职位标题
            jobdata['positionName'] = jobinfo['positionName']
            #职位的发布时间
            jobdata['publishTime'] = jobinfo['formatCreateTime']
            #公司名称
            jobdata['companyName'] = jobinfo['companyShortName']
            #薪资
            jobdata['salary'] = jobinfo['salary']
            #工作经验
            jobdata['workYear'] = jobinfo['workYear']
            #学历
            jobdata['education'] = jobinfo['education']
            #公司类型
            jobdata['industry'] = jobinfo['industryField']
            #融资
            jobdata['stage'] = jobinfo['financeStage']
            #人数
            jobdata['companySize'] = jobinfo['companySize']
            #福利
            jobdata['fuli'] = ','.join(jobinfo['companyLabelList'])
            #招聘诱惑
            jobdata['positionAdvantage'] = jobinfo['positionAdvantage']

            save_data_to_db(jobdata)
            #print(jobdata)

        #判断是否需要发起下一次请求
        #取出当前页码
        cur_page = int(data['content']['pageNo'])
        #每页返回多少条数据
        page_size = int(data['content']['pageSize'])
        #职位总数
        totalcount = int(data['content']['positionResult']['totalCount'])
        if cur_page*page_size < totalcount:
            #下一页的页码
            next_page = cur_page+1
            print('继续发起请求第'+str(next_page)+'页')
            formdata['pn'] = next_page
            time.sleep(1)
            lagouspider(url,formdata)
    else:
        print('请求不成功,休息一会继续发起请求')
        time.sleep(10)
        print('重新发起第'+str(formdata['pn'])+'页请求')
        lagouspider(url,formdata)

def load_page_data(url,formdata):
    """
    发起请求(下载器)
    :param url:
    :param formdata:
    :return:
    """
    #将表单数据转为web服务器能识别的url编码格式的bytes类型的数据
    form_data = parse.urlencode(formdata).encode('utf-8')
    #设置请求头
    req_headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_c%2B%2B?labelWords=&fromSearch=true&suginput=',
    }
    #构建一个request对象
    req = request.Request(url,headers=req_headers,data=form_data)
    #发起请求
    response = request.urlopen(req)
    if response.status == 200:
        return response.read().decode('utf-8')

def save_data_to_db(jobdata):
    """
    存储数据
    :param jobdata: 对应的是一个字典（存放的是职位信息）
    :return:
    """

    sql = """
    INSERT INTO lagou (%s)
    VALUES (%s)
    """ % (
        ','.join(jobdata.keys()),
        ','.join(["%s"]*len(jobdata))
    )
    try:
        cursor.execute(sql,list(jobdata.values()))
        mysql_client.commit()
    except Exception as err:
        print(err)
        mysql_client.rollback()

if __name__ == '__main__':

    #数据库连接
    """
    host=None, user=None, password="",
    database=None, port=0,
    charset=''
    """
    mysql_client = pymysql.Connect(
        '127.0.0.1','root','ljh1314',
        '1712B',3306,charset='utf8',
    )
    #创建游标(执行sql语句)
    cursor = mysql_client.cursor()

    #目标url
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

    #要提交的参数
    formdata = {
        'first': 'true',
        'pn': 1,
        'kd': 'c++',
    }
    lagouspider(url,formdata)




