# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:52:25 2017

@author: Nzix
"""

import urllib2
import re

members={
    u"井口眞緒":[u"いぐち まお","iguchi-mao"],
    u"潮紗理菜":[u"うしお さりな","ushio-sarina"],
    u"柿崎芽実":[u"かきざき めみ","kakizaki-memi"],
    u"影山優佳":[u"かげやま ゆうか","kageyama-yuuka"],
    u"加藤史帆":[u"かとう しほ","katou-shiho"],
    u"齊藤京子":[u"さいとう きょうこ","saitou-kyouko"],
    u"佐々木久美":[u"ささき くみ","sasaki-kumi"],
    u"佐々木美玲":[u"ささき みれい","sasaki-mirei"],
    u"高瀬愛奈":[u"たかせ まな","takase-mana"],
    u"高本彩花":[u"たかもと あやか","takamoto-ayaka"],
    u"長濱ねる":[u"ながはま ねる","nagahama-neru"],
    u"東村芽依":[u"ひがしむら めい","higashimura-mei"],
    u"石森虹花":[u"いしもり にじか","ishimori-nijika"],
    u"今泉佑唯":[u"いまいずみ ゆい","imaizumi-yui"],
    u"上村莉菜":[u"うえむら りな","uemura-rina"],
    u"尾関梨香":[u"おぜき りか","ozeki-rika"],
    u"織田奈那":[u"おだ なな","oda-nana"],
    u"小池美波":[u"こいけ みなみ","koike-minami"],
    u"小林由依":[u"こばやし ゆい","kobayashi-yui"],
    u"齋藤冬優花":[u"さいとう ふゆか","saitou-fuyuka"],
    u"佐藤詩織":[u"さとう しおり","satou-shiori"],
    u"志田愛佳":[u"しだ まなか","shida-manaka"],
    u"菅井友香":[u"すがい ゆうか","sugai-yuuka"],
    u"鈴本美愉":[u"すずもと みゆ","suzumoto-miyu"],
    u"長沢菜々香":[u"ながさわ ななこ","nagasawa-nanako"],
    u"土生瑞穂":[u"はぶ みづほ","habu-mizuho"],
    u"原田葵":[u"はらだ あおい","harada-aoi"],
    u"平手友梨奈":[u"ひらて ゆりな","hirate-yurina"],
    u"守屋茜":[u"もりや あかね","moriya-akane"],
    u"米谷奈々未":[u"よねたに ななみ","yonetani-nanami"],
    u"渡辺梨加":[u"わたなべ りか","watanabe-rika"],
    u"渡邉理佐":[u"わたなべ りさ","watanabe-risa"]
}


url = 'http://www.keyakizaka46.com/s/k46o/search/artist?ima=0000'
headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8' }
request = urllib2.Request(url=url, headers=headers)
response = urllib2.urlopen(request)
page_data = response.read()

filting = re.findall(r'<li data-member="(\d{2})">\s*?<a[^>]+?>\s*?<img src="([^"]+?)"\s*?/>\s*?<p class="name">\s+([^<]+?)\s+</p>\s*<p class="furigana">\s+([^<]+?)\s+</p></a>\s*</li>',page_data)

for item in filting:
    #print item[0]
    name =  re.sub(r" ","",item[2]).decode("utf-8")
    if name in members:
        if members[name][0] != item[3].decode("utf-8"):
            print name + "'s furigana check with error " + members[name][0] + " -- " + item[3].decode("utf-8")
            continue
    else:
        print name + " this name is not in dict"
        continue

    request = urllib2.Request(url=item[1], headers=headers)
    response = urllib2.urlopen(request)
    photo_data = response.read()
    
    f=open("d:\\update\\" + members[name][1] + ".jpg" , "wb" )
    f.write(photo_data)
    f.close()
    
    print "get " + name + "'s official pic"
    
            