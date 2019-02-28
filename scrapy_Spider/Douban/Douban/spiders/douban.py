# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/people/189212653/']

    def start_requests(self):
        cookie = 'll="108288"; bid=kibLwdDlEQE; ps=y; douban-profile-remind=1; push_doumail_num=0; push_noty_num=0; _ga=GA1.2.1335571132.1545293105; douban-fav-remind=1; _vwo_uuid_v2=DB72DB42F885B8E0515FD052CED1F143A|4556d3a69edd3b1b8bc2025fc256c5eb; __utmz=30149280.1545830967.8.7.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/register_success; __utmv=30149280.18921; ue="626204777@qq.com"; dbcl2="189212653:b8IPG14cjbo"; _gid=GA1.2.1290099379.1546505502; ck=flTA; ap_v=0,6.0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1546505512%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3D18518753265%26redir%3Dhttps%253A%252F%252Fwww.douban.com%252Fgallery%252F%26source%3Dmain%26error%3D1013%22%5D; _pk_ses.100001.8cb4=*; _pk_id.100001.8cb4=4a0986395fefc45f.1545293096.10.1546505513.1545871751.; __utma=30149280.1335571132.1545293105.1545871503.1546505514.11; __utmc=30149280; __utmt=1; __utmb=30149280.2.10.1546505514',
        cookies_dict = {cookie.split('=')[0]: cookie.split('=')[1]}

        # 注意：
        # 1、模拟用户请求的时候，一定要注意将cookie传递到Request参数里面,传到headers里面是不生效的
        # 2、在settings里面的COOKIES_ENABLED设置为True，默认下一次请求带cookie
        for url in self.start_urls:
            yield scrapy.Request(url=url, cookies=cookies_dict, callback=self.parse_data)

    def parse(self, response):
        pass

    def parse_data(self, response):
        print(response.status)

        with open('douban.html') as f:
            f.write(response.text)
