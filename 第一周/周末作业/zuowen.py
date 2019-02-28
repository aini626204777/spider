import requests, re, os


class zuowenSpider(object):
    def __init__(self):
        self.url = 'https://www.99zuowen.com/xiaoxuezuowen/ynjzuowen/'
        self.req_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

    def load(self, url, headers):
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            result = re.compile(
                'line_bt"></i><span.*?class="right"><a target="_blank" href="(.*?)".*?title="更多">更多</a></span><h3>(.*?)</h3></div>',
                re.S)
            data = re.findall(result, response.text)
            data.pop(-2)
            for i in data:
                url = re.compile('/xiaoxuezuowen/(.*?)/', re.S)
                result_url = re.findall(url, list(i)[0])
                details_url = 'https://www.99zuowen.com/xiaoxuezuowen/' + ''.join(result_url) + '/'
                folder_name = list(i)[1]
                isExists = os.path.exists(folder_name)
                if not isExists:
                    os.makedirs(folder_name)
                    self.request_details(url=details_url, folder_name=folder_name)
                else:
                    self.request_details(url=details_url, folder_name=folder_name)

    def request_details(self,url,folder_name):
        if url == 'https://www.99zuowen.com/xiaoxuezuowen/youji/':
            response = requests.get(url=url, headers=self.req_headers)
            if response.status_code == 200:
                result = re.compile('游记作文</a><a.*?href="(.*?)".*?class="ulink"', re.S)
                data = re.findall(result, response.text)
                for zuowen_details_url in data:
                    response = requests.get(url=zuowen_details_url, headers=self.req_headers)
                    if response.status_code == 200:
                        result = re.compile(
                            'class="title"><h1>(.*?)</h1></div>.*?title="本文来源于www.99zuowen.com">(.*?)</a>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<p>(.*?)</div>',
                            re.S)
                        data = re.findall(result, response.text)
                        for i in data:
                            zuowen_data = {}
                            zuowen_data['title'] = i[0]
                            zuowen_data['address'] = i[1]
                            zuowen_data['author'] = i[2]
                            zuowen_data['date'] = i[3]
                            zuowen_data['content'] = re.sub('[</p>\r<p>\r\t&helli;dquo]', '', i[4])
                            if not os.path.exists(os.getcwd()):
                                os.makedirs(folder_name)
                                file_name = os.getcwd() + '/' + folder_name + '/' + zuowen_data['title'] + '.txt'
                                f = open(file_name, 'w')
                                f.write('标题：' + zuowen_data['title'] + '\n' + '来源：' + zuowen_data['address'] + '\n' +
                                        zuowen_data['author'] + '\n' + '发布时间：' + zuowen_data['date'] + '\n' + zuowen_data[
                                            'content'])
                            else:
                                file_name = os.getcwd() + '/' + folder_name + '/' + zuowen_data['title'] + '.txt'
                                f = open(file_name, 'w')
                                f.write('标题：' + zuowen_data['title'] + '\n' + '来源：' + zuowen_data['address'] + '\n' +
                                        zuowen_data['author'] + '\n' + '发布时间：' + zuowen_data['date'] + '\n' + zuowen_data[
                                            'content'])

        else:
            response = requests.get(url=url, headers=self.req_headers)
            if response.status_code == 200:
                result = re.compile('<li.*?class="lis"><h4><a.*?href="(.*?)".*?title=', re.S)
                data = re.findall(result, response.text)
                for zuowen_details_url in data:
                    response = requests.get(url=zuowen_details_url, headers=self.req_headers)
                    if response.status_code == 200:
                        result = re.compile(
                            'class="title"><h1>(.*?)</h1></div>.*?title="本文来源于www.99zuowen.com">(.*?)</a>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<p>(.*?)</div>',
                            re.S)
                        data = re.findall(result, response.text)
                        for i in data:
                            zuowen_data = {}
                            zuowen_data['title'] = i[0]
                            zuowen_data['address'] = i[1]
                            zuowen_data['author'] = i[2]
                            zuowen_data['date'] = i[3]
                            zuowen_data['content'] = re.sub('[</p>\r<p>\r\t&helli;dquo]', '', i[4])
                            if not os.path.exists(os.getcwd()):
                                os.makedirs(folder_name)
                                file_name = os.getcwd() + '/' + folder_name + '/' + zuowen_data['title'] + '.txt'
                                f = open(file_name, 'w')
                                f.write('标题：' + zuowen_data['title'] + '\n' + '来源：' + zuowen_data['address'] + '\n' +
                                        zuowen_data['author'] + '\n' + '发布时间：' + zuowen_data['date'] + '\n' + zuowen_data[
                                            'content'])
                            else:
                                file_name = os.getcwd() + '/' + folder_name + '/' + zuowen_data['title'] + '.txt'
                                f = open(file_name, 'w')
                                f.write('标题：' + zuowen_data['title'] + '\n' + '来源：' + zuowen_data['address'] + '\n' +
                                        zuowen_data['author'] + '\n' + '发布时间：' + zuowen_data['date'] + '\n' + zuowen_data[
                                            'content'])


if __name__ == '__main__':
    zuowen = zuowenSpider()
    zuowen.load(url=zuowen.url, headers=zuowen.req_headers)
