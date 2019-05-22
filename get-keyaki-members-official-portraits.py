# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:52:25 2017

@author: Nzix
"""


import re
import os
import requests

from members import KEYAKIZAKA
import wget

URL = 'http://www.keyakizaka46.com/s/k46o/search/artist?ima=0000'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'}
OUTPUT_FOLDER = './tmp/keyaki/portraits/'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

filting = re.findall(
    r'<li data-member="(\d{2})">\s*?<a[^>]+?>\s*?<img src="([^"]+?)"\s*?/>\s*?<p class="name">\s+([^<]+?)\s+</p>\s*<p class="furigana">\s+([^<]+?)\s+</p></a>\s*</li>',
    requests.get(url=URL, headers=HEADERS).text)

for item in filting:
    name = re.sub(r" ", "", item[2])
    if name in KEYAKIZAKA:
        if KEYAKIZAKA[name][0] == item[3]:
            filepath = os.path.abspath(os.path.join(OUTPUT_FOLDER, '{}.jpg'.format(KEYAKIZAKA[name][1])))
            if not os.path.isfile(filepath):
                wget.download(url=item[1], out=filepath)
        else:
            print('{}\'s furigana check with error {} -- {}'.format(name, KEYAKIZAKA[name][0], item[3]))
    else:
        print('{} this name is not in dict'.format(name))
