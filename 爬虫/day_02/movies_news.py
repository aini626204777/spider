import urllib.request as request
import urllib.parse as parse
# import ssl

response = request.urlopen('http://www.1905.com/film/?fr=homepc_menu_news')

r = response.read().decode('utf-8')

print(response.read().decode('utf-8'))

f = open('movie.html', 'w')
f.write(r)
