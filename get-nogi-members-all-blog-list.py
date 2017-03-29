# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 14:51:04 2017

@author: Nzix
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re
import collections
import urllib2
import operator
import json
import datetime

regex = r'''<div class="unit">[\s\S]+?<span class="yearmonth">([\s\S]+?)</span>[\s\S]+?<span class="dd1">([\s\S]+?)</span>[\s\S]+?<span class="dd2">([\s\S]+?)</span>[\s\S]+?<span class="author">([\s\S]+?)</span>[\s\S]+?<a href="([^"]+?)"[^>]+?>([\s\S]+?)</a>[\s\S]+?<div class="entrybodyin">\s*([\s\S]+?)\s*</div>[\s\S]+?<div class="kijifoot">([\s\S]+?)</div>'''
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

urlnamedict = {
    "秋元真夏":"manatsu.akimoto",
    "生田絵梨花":"erika.ikuta",
    "生駒里奈":"rina.ikoma",
    "伊藤かりん":"karin.itou",
    "伊藤純奈":"junna.itou",
    "伊藤万理華":"marika.ito",
    "井上小百合":"sayuri.inoue",
    "衛藤美彩":"misa.eto",
    "川後陽菜":"hina.kawago",
    "川村真洋":"mahiro.kawamura",
    "北野日奈子":"hinako.kitano",
    "齋藤飛鳥":"asuka.saito",
    "斎藤ちはる":"chiharu.saito",
    "斉藤優里":"yuuri.saito",
    "相楽伊織":"riori.sagara",
    "桜井玲香":"reika.sakurai",
    "佐々木琴子":"kotoko.sasaki",
    "白石麻衣":"mai.shiraishi",
    "新内眞衣":"mai.shinuchi",
    "鈴木絢音":"ayane.suzuki",
    "高山一実":"kazumi.takayama",
    "寺田蘭世":"ranze.terada",
    "中田花奈":"kana.nakada",
    "中元日芽香":"himeka.nakamoto",
    "西野七瀬":"nanase.nishino",
    "能條愛未":"ami.noujo",
    "橋本奈々未":"nanami.hashimoto",
    "樋口日奈":"hina.higuchi",
    "星野みなみ":"minami.hoshino",
    "堀未央奈":"miona.hori",
    "松村沙友理":"sayuri.matsumura",
    "山崎怜奈":"rena.yamazaki",
    "若月佑美":"yumi.wakatsuki",
    "渡辺みり愛":"miria.watanabe",
    "和田まあや":"maaya.wada",
    "３期生":"third",
    "研究生":"kenkyusei",
    "スタッフブログ":"staff"
}

member = urlnamedict["橋本奈々未"]#you can change this
page = 1
month = 11
year = 2011

content_first=[]
rawlist=[]

thisyear = datetime.datetime.now().year
thismonth = datetime.datetime.now().month

while year!=2017 or month != thismonth:
    
    if month == 13:
        month = 1      
        year = year + 1

    url = "http://blog.nogizaka46.com/%s/smph/?p=%s&d=%s"%(member, str(page), str(year)+str(month).zfill(2))
    
    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request) 
    if response.geturl() != url:#it might be redirected
        month = month + 1
        page = 1
        continue    
    data = response.read().decode("utf-8")
    content=re.findall(regex,data)

    if page == 1:
        content_first = content
    elif content_first == content:
        month = month + 1
        page = 1
        continue
    
    print str(year)+str(month).zfill(2)+" page"+str(page)
    for i in xrange(len(content)-1,-1,-1):
        oneblog = collections.OrderedDict()    
        oneblog["post"] = content[i][7][0:16]
        oneblog["author"] = content[i][3]
        oneblog["title"] = content[i][5]
        oneblog["summary"] = content[i][6]
        oneblog["url"] = content[i][4]
        rawlist.append(oneblog)
        
    page = page + 1

sortedlist = sorted(rawlist, key = operator.itemgetter('post') ,reverse=True)

print "total " + len(sortedlist)

name = member.split(".")[0]
f = open("d:\\" + name + ".json", 'w')
f.write(json.dumps(sortedlist,ensure_ascii=False,sort_keys=False,indent=1))
f.close()
