from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
import time


number = 1
prev = ''
url = 'http://xkcd.com/'
while not url.endswith('#'):

    print(str(number))
    number += 1

    url = 'http://xkcd.com/' + prev

    res = requests.get(url).content
    soup = BeautifulSoup(res,'html.parser')
    x = soup.select_one('div #comic img')
    padrao = re.compile(r'/.*g')
    padrao2 = re.compile(r'\.\w*\s')

    p1 = padrao.search(x['srcset'])
    p2 = 'http:' + p1.group()
    p3 = padrao2.search(x['srcset'])

    dt = datetime.today().strftime('%y%m%d_%H%M%s')

    dtp3 = dt + p3.group()

    p33 = p3.group().split(' ')
    p33 = p33[0].split('.')
    path2 = 'downloads/' + p33[-1] + '/' + dtp3

    path2 = path2.split(' ')
    res2 = requests.get(p2).content
    with open(path2[0],'wb') as book:
        book.write(res2)

#prev

    prev = soup.select('.comicNav a')[1]['href']

print(datetime.today().strftime('%y-%m-%d_%H:%M:%s'))
print('Acabou')
