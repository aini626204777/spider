from urllib import request




url = 'https://www.douban.com/people/175417123/'
req_headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    'Cookie':'ll="108288"; bid=kibLwdDlEQE; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1545293096%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1335571132.1545293105.1545293105.1545293105.1; __utmc=30149280; __utmz=30149280.1545293105.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; ps=y; dbcl2="175417123:yY3DyEelGJE"; ck=FxtM; douban-profile-remind=1; _pk_id.100001.8cb4=4a0986395fefc45f.1545293096.1.1545293329.1545293096.; push_doumail_num=0; ap_v=0,6.0; __utmv=30149280.17541; __utmb=30149280.3.10.1545293105; push_noty_num=7'
}

req = request.Request(url,headers=req_headers)

response = request.urlopen(req)
if response.status == 200:
    response = response.read().decode('utf8')
    print(response)