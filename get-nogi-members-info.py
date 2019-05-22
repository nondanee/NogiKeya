#! /usr/local/bin/python3.7


from datetime import datetime
import json
import re

import requests
from members import NOGIZAKA

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}


def pageget(url):

    data = requests.get(url=url, headers=HEADERS).text
    block = re.search(r'''<div id="container">([\s\S]+?)</div>\s*<\!--▼スケジュール-->''', data).group(1)

    valid = re.findall(
        r'''<div class="pic"><img src="([^"]+)"[\s\S]+?<h3>([^<]+?)<span class="sub">([^<]+?)</span></h3>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<div class="status">([\s\S]+)''',
        block)[0]

    status = re.sub(r'<[^>]+?>', " ", valid[7])
    status = re.sub(r'^\s*', "", status)
    status = re.sub(r'\s*$', "", status)
    status = re.sub(r'\s+', " ", status)
    name = re.sub(r' ', '', valid[1])

    return dict(
        name=name,
        kana=valid[2][1:-1],
        rome=NOGIZAKA[name].split('.')[1] + '-' + NOGIZAKA[name].split('.')[0],
        birthdate=valid[3],
        bloodtype=valid[4],
        constellation=valid[5],
        height=valid[6],
        status=status,
        portrait=re.sub(r'\?\w+$', '', valid[0]),
        link=url)


def getlist():
    url = "http://www.nogizaka46.com/smph/member/"
    data = requests.get(url=url, headers=HEADERS).text
    listblock = re.search(r'''<div class="main">([\s\S]+)</div><\!--member end-->''', data).group(1)
    urllist = re.findall(r'''\./detail/\w+\.php''', listblock)
    return [url+line[1:] for line in urllist]


starttime = datetime.now()
with open("allmembers.json", 'w') as writer:
    for record in sorted([pageget(url) for url in getlist()], key=lambda x: x['kana']):
        writer.write(json.dumps(record, ensure_ascii=False, sort_keys=False, indent=4))
        writer.write('\n')
executetime = datetime.now()-starttime

print(str(executetime.seconds+executetime.microseconds/1000000)+"ms")
