import requests
import http.cookiejar
# 1. 创建session对象，可以保存Cookie值
ssion = requests.session()

# 2. 处理 headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    #'Cookie': 'anonymid=ji33y97v-g3mgln; XNESSESSIONID=abcfyPaUs-XgU6F14ivpw; depovince=GW; _r01_=1; ick_login=589b6824-c373-4cfa-8554-02712dff92d0; ick=15c669ff-355e-41a0-a35c-7dc042ed2773; t=a8023a669d14a07b9c713eea02a0f5881; societyguester=a8023a669d14a07b9c713eea02a0f5881; id=966301461; xnsid=2ad8f8cc; jebecookies=82ec54ea-e09e-4ceb-9eef-0dda9d0005d5|||||; ch_id=10016; jebe_key=5da127a4-fd8e-4ad2-b270-ab63f042279f%7C1d68c41bf49c51561d8a8de9c8660e6f%7C1528289573881%7C1%7C1528289558434; wpsid=15215316961556; wp_fold=0'
}


# 3. 需要登录的用户名和密码
data = {"email":"15110500442", "password":"sjl111111"}

# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://www.renren.com/PLogin.do", data = data)

# 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = ssion.get("http://www.renren.com/966301461/profile")
with open('renre.txt','a',encoding='utf-8') as f:
    f.write(response.text)


# 6. 打印响应内容
print(response.text)