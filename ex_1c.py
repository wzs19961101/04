from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

d = pd.DataFrame({'name':[], 'genres':[], 'years active':[]})

url = 'https://en.wikipedia.org/wiki/Queen_(band)'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    name = bs.find('h1').text
except:
    name = ''

try:
    genres = bs.find('th',string = 'Genres').next_sibling.text
except:
    genres = ''

try:
    years_active = bs.find('th',string = 'Years active').next_sibling.text
except:
    years_active = ''


Q = {'name':name, 'genres':genres, 'years active':years_active}

d = d.append(Q, ignore_index = True)

print(d)
