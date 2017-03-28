# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:07:54 2017

@author: Nzix
"""

import urllib2
import re

members={
    u"秋元真夏":[u"あきもと まなつ","akimoto-manatsu"],
    u"生田絵梨花":[u"いくた えりか","ikuta-erika"],
    u"生駒里奈":[u"いこま りな","ikoma-rina"],
    u"伊藤万理華":[u"いとう まりか","itou-marika"],
    u"井上小百合":[u"いのうえ さゆり","inoue-sayuri"],
    u"衛藤美彩":[u"えとう みさ","etou-misa"],
    u"川後陽菜":[u"かわご ひな","kawago-hina"],
    u"川村真洋":[u"かわむら まひろ","kawamura-mahiro"],
    u"齋藤飛鳥":[u"さいとう あすか","saitou-asuka"],
    u"斎藤ちはる":[u"さいとう ちはる","saitou-chiharu"],
    u"斉藤優里":[u"さいとう ゆうり","saitou-yuuri"],
    u"桜井玲香":[u"さくらい れいか","sakurai-reika"],
    u"白石麻衣":[u"しらいし まい","shiraishi-mai"],
    u"高山一実":[u"たかやま かずみ","takayama-kazumi"],
    u"中田花奈":[u"なかだ かな","nakada-kana"],
    u"中元日芽香":[u"なかもと ひめか","nakamoto-himeka"],
    u"西野七瀬":[u"にしの ななせ","nishino-nanase"],
    u"能條愛未":[u"のうじょう あみ","noujou-ami"],
    u"橋本奈々未":[u"はしもと ななみ","hashimoto-nanami"],
    u"樋口日奈":[u"ひぐち ひな","higuchi-hina"],
    u"星野みなみ":[u"ほしの みなみ","hoshino-minami"],
    u"松村沙友理":[u"まつむら さゆり","matsumura-sayuri"],
    u"若月佑美":[u"わかつき ゆみ","wakatsuki-yumi"],
    u"和田まあや":[u"わだ まあや","wada-maaya"],
    u"伊藤かりん":[u"いとう かりん","itou-karin"],
    u"伊藤純奈":[u"いとう じゅんな","itou-junna"],
    u"北野日奈子":[u"きたの ひなこ","kitano-hinako"],
    u"相楽伊織":[u"さがら いおり","sagara-iori"],
    u"佐々木琴子":[u"ささき ことこ","sasaki-kotoko"],
    u"新内眞衣":[u"しんうち まい","shinuchi-mai"],
    u"鈴木絢音":[u"すずき あやね","suzuki-ayane"],
    u"寺田蘭世":[u"てらだ らんぜ","terada-ranze"],
    u"堀未央奈":[u"ほり みおな","hori-miona"],
    u"山崎怜奈":[u"やまざき れな","yamazaki-rena"],
    u"渡辺みり愛":[u"わたなべ みりあ","watanabe-miria"],
    u"伊藤理々杏":[u"いとう りりあ","itou-riria"],
    u"岩本蓮加":[u"いわもと れんか","iwamoto-renka"],
    u"梅澤美波":[u"うめざわ みなみ","umezawa-minami"],
    u"大園桃子":[u"おおぞの ももこ","oozono-momoko"],
    u"久保史緒里":[u"くぼ しおり","kubo-shiori"],
    u"阪口珠美":[u"さかぐち たまみ","sakaguchi-tamami"],
    u"佐藤楓":[u"さとう かえで","satou-kaede"],
    u"中村麗乃":[u"なかむら れの","nakamura-reno"],
    u"向井葉月":[u"むかい はづき","mukai-hazuki"],
    u"山下美月":[u"やました みづき","yamashita-mizuki"],
    u"吉田綾乃クリスティー":[u"よしだ あやの くりすてぃー","yoshida-ayano-christie"],
    u"与田祐希":[u"よだ ゆうき","yoda-yuuki"]
}


url = 'http://www.nogizaka46.com/member/'
headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8' }
request = urllib2.Request(url=url, headers=headers)
response = urllib2.urlopen(request)
page_data = response.read()

filting = re.findall(r'<div class="[^"]+"><a href="([^"]+)">[\s\S]+?<span class="main">([^<]+?)</span><span class="sub">([^<]+?)</span>[\s\S]+?</div>',page_data)

for item in filting:
    name =  re.sub(r" ","",item[1]).decode("utf-8")
    if name in members:
        if members[name][0] != item[2].decode("utf-8"):
            print name + "'s furigana check with error " + members[name][0] + " -- " + item[3].decode("utf-8")
            continue
    else:
        print name + " this name is not in dict"
        continue

    photo_link = "http://img.nogizaka46.com/www/member/img/" + re.search(r'/(\w+)\.php',item[0]).group(1)+ "_prof.jpg"
#    url =re.sub(r'^\.',"http://www.nogizaka46.com/member",item[0])
#    request = urllib2.Request(url=url, headers=headers)
#    response = urllib2.urlopen(request)
#    page_data = response.read()
#    
#    if re.search(r'<div id="profile" class="clearfix">\s<img src="([^"]+?)"',page_data) != None: 
#        photo_link = re.search(r'<div id="profile" class="clearfix">\s<img src="([^"]+?)"',page_data).group(1)
#    else:
#        print "can't find portrait url (" + name +")"
#        continue
 
    request = urllib2.Request(url=photo_link, headers=headers)
    response = urllib2.urlopen(request)
    photo_data = response.read()
    
    f=open("d:\\update2\\" + members[name][1] + ".jpg" , "wb" )
    f.write(photo_data)
    f.close()
    
    print "get " + name + "'s official pic"
    
            