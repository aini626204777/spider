# urllib.error的容错

import urllib.error
import urllib.request
import ssl
req = urllib.request.Request('http://www.gfdsgfd.com/fdsagdsagdsa')
content = ssl._create_unverified_context

try:
    response = urllib.request.urlopen(req,context=content)
    print('成功')
except urllib.error.HTTPError as err:
    print(response.code)


except urllib.error.URLError as err:
    print('失败原因'+err.reason)

