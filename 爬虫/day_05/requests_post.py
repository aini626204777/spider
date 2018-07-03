# post请求
# 以拉钩网为例

import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first': 'false',
    'pn': '1',
    'kd': 'php',
}
headers = {
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '23',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Cookie': 'user_trace_token=20180530141218-5edfc427-42e9-46c1-8b20-117c60a1b3f7; _ga=GA1.2.1292977445.1527660739; LGUID=20180530141219-688b2604-63d0-11e8-81f1-525400f775ce; _gid=GA1.2.1668034658.1528251093; WEBTJ-ID=20180606101133-163d2dd1028fe-0b8106b179b10c-3961430f-1327104-163d2dd1029338; PRE_HOST=www.baidu.com; LGSID=20180606101147-f78f56f8-692e-11e8-9238-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K600000-SwTdAzCGTIhHKlz9gX_IffUKtM-QRT2rZVtybKWoZKFynC0gYvq3jiAE8HpjmtdhWFERp_drZKwqMr_0Is_WT_nRzhu7g-ayZbQMEc_4acZdppo3N9KiVV4nX0ckRTK0pv3e3q1qpW690Dcf_N8kh4i4szjpr66QVEO7AVQRFs.7b_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzL4XNPIIhExzLu2SMcM-sSxH9vX8ZuEsSXej_qT5o43x5ksSEzseldPHV2XgZJyAp7WWgklX-f.U1Yk0ZDqs2v4VnL30ZKGm1Yk0Zfqs2v4VnL30A-V5HcsP0KM5yF8nj00Iybqmh7GuZR0TA-b5HD0mv-b5Hn3PfKVIjYknjDLg1DsnH-xnH0zndt1njDdg1nvnjD0pvbqn0KzIjYvn6K-pyfqnHfYnNtznH04P-tzPWndn7tznjb1n0KBpHYznjf0UynqP1nsnHfLPWbYg1Dsnj7xnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5Hc3nHbdPHRzPH60UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5HD0uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0ZwdT1Y1n16dPHTsnWR4Pjm3njTsP1cs0ZF-TgfqnHRzrjcdnH04nj01PfK1pyfquycLrHI9PHbsnj0snW0drfKWTvYqwj9KfW6kwH9APHFDfHFjfsK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1nHb4nWKxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5HmYPjDz%26ck%3D4210.2.135.254.559.258.561.273%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.2.0.1.301.0%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1078%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_bj_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; JSESSIONID=ABAAABAAADEAAFIBFF5865C1F4AB9081FC6B6D3083F4505; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528252357,1528252518,1528252527,1528252669; TG-TRACK-CODE=index_search; SEARCH_ID=bd1b6506ed664c34849d55f2119509fa; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528252672; LGRID=20180606103752-9c2a307f-6932-11e8-9379-5254005c3644',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_php?labelWords=&fromSearch=true&suginput=',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
print(response.text)


# 使用json()
data = response.json()
print(type(data))
print(data['content']['hrInfoMap']['2305269'])

