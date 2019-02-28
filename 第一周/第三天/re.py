import re

http = 'https://company.zhaopin.com/CZ641633520.htm'
pat = re.compile('https.+')

result = re.match(pat,http)
print(result.group())