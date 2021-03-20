from urllib import request
from bs4 import BeautifulSoup as BS
import re


url = 'https://en.wikipedia.org/wiki/Lists_of_musicians'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tag1 = bs.find_all('a', {'title':re.compile('List of R&.*')})
tag2 = bs.find_all('a', {'title':re.compile('List of r.*')})
tags = tag1+tag2

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)
