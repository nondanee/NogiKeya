# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:07:54 2017

@author: Nzix
"""

import os
import re

import requests

from members import NOGIZAKA
import wget

MEMBER_URL = 'http://www.nogizaka46.com/member/'
PHOTO_URL = 'http://img.nogizaka46.com/www/member/img/{}_prof.jpg'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'}
OUTPUT_FOLDER = './tmp/nogi/portraits/'
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

filting = re.findall(
    r'<div class="[^"]+"><a href="([^"]+)">[\s\S]+?<span class="main">([^<]+?)</span><span class="sub">([^<]+?)</span>[\s\S]+?</div>',
    requests.get(url=MEMBER_URL, headers=HEADERS).text)

for item in filting:
    name = re.sub(r" ", "", item[1])
    if name in NOGIZAKA:
        if NOGIZAKA[name][0] == item[2]:
            filepath = os.path.abspath(os.path.join(OUTPUT_FOLDER, '{}.jpg'.format(NOGIZAKA[name][1])))
            if not os.path.isfile(filepath):
                wget.download(url=PHOTO_URL.format(re.search(r'/(\w+)\.php', item[0]).group(1)), out=filepath)
        else:
            print(name + "'s furigana check with error " + NOGIZAKA[name][0] + " -- " + item[3].decode("utf-8"))
    else:
        print(name + " this name is not in dict")
