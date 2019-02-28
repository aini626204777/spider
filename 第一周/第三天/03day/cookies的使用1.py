from urllib import request
# 目标url：
# https://www.douban.com/people/175417123/

url = 'https://www.douban.com/people/175417123/'

# 设置请求头
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie': 'bid=a5HEJxBlOLY; douban-fav-remind=1; ll="108288"; _vwo_uuid_v2=D4EC41D965B5FF84E814BF48AE34386A5|f6047e628a6acc98722e3100dfbc399c; __yadk_uid=KpfeK1cgib5IWMKWvG66MnJMbonYvDZa; _ga=GA1.2.36315712.1531837787; douban-profile-remind=1; push_doumail_num=0; push_noty_num=0; __utmv=30149280.17541; _gid=GA1.2.2070226630.1545227516; ps=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1545292749%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DqpgHwc2FYGfOrGzt4yK3ZwwbraVm_oED80whnivpFaC3kA5IvGnUfQ9FSRZBOEVh%26wd%3D%26eqid%3D85ed620e000397aa000000065c1b4bc8%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.36315712.1531837787.1545227511.1545292752.48; __utmc=30149280; __utmz=30149280.1545292752.48.37.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="175417123:yY3DyEelGJE"; ck=FxtM; ap_v=0,6.0; _pk_id.100001.8cb4=7521abce5497fc2c.1531837784.39.1545292778.1545228853.; __utmb=30149280.7.10.1545292752',
}

req = request.Request(url=url,headers=req_header)

response = request.urlopen(req)

if response.status == 200:
    with open('douban.html','w') as file:
        file.write(response.read().decode('utf-8'))
