from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/List_of_rock_music_performers'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


tag1 = bs.find_all('a', {'title':re.compile('Q.*')})
tag2 = bs.find_all('a', {'title':re.compile('The Q .*')})
tags = tag1+tag2

links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)
