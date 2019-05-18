# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:51:04 2017

@author: Nzix
"""

from datetime import datetime
import json
import os
import re
import random
import time
from tqdm import tqdm
from typing import Generator
import requests


from members import NOGIZAKA

REGEX = r'''<div class="unit">[\s\S]+?<span class="yearmonth">([\s\S]+?)</span>[\s\S]+?<span class="dd1">([\s\S]+?)</span>[\s\S]+?<span class="dd2">([\s\S]+?)</span>[\s\S]+?<span class="author">([\s\S]+?)</span>[\s\S]+?<a href="([^"]+?)"[^>]+?>([\s\S]+?)</a>[\s\S]+?<div class="entrybodyin">\s*([\s\S]+?)\s*</div>[\s\S]+?<div class="kijifoot">([\s\S]+?)</div>'''
HEADERS = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 Instagram 10.10.0 (iPhone5,2; iOS 10_2_1; ja_JP; ja-JP; scale=2.00; gamut=normal; 640x1136)"}
BLOG_URL = 'http://blog.nogizaka46.com/{member}/smph/?p={page_no}&d={year}{month}'
OUTPUT_FOLDER = os.path.abspath('./tmp/nogi/blog/')
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def get_blog_post(member: str) -> Generator[dict, None, None]:
    page = 1
    year, month = 2011, 10
    current_date = datetime.now()

    while year != current_date.year or month != current_date.month + 1:
        if month > 12:
            month = 1
            year += 1

        url = BLOG_URL.format(member=member[1], page_no=page, year=year, month=str(month).zfill(2))
        contents = re.findall(REGEX, requests.get(url, headers=HEADERS).text)

        if page == 1:
            content_first = contents
        elif content_first == contents:
            month += 1
            page = 1
            continue

        for post in contents:
            yield dict(title=post[6], created_at='/'.join([post[0], post[1]]), author=post[3], url=post[4])
        page += 1


if __name__ == "__main__":
    for name, member in NOGIZAKA.items():
        with open(os.path.join(OUTPUT_FOLDER, '{}.json'.format(member[1].replace('.', '_'))), 'w') as writer:
            for blog in tqdm(get_blog_post(member), postfix=name):
                writer.write(json.dumps(blog, ensure_ascii=False, sort_keys=False))
                writer.write('\n')
        sleep_length = random.choice(range(1, 11))
        print('sleep: %s' % sleep_length)
        time.sleep(sleep_length)
