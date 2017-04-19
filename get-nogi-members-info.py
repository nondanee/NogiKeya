#! /usr/local/bin/python3.5

import asyncio
import aiohttp
import re
import os 
import json
import operator
import collections
import urllib.request
import datetime

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}

membersdict={
    u"秋元真夏":"akimoto-manatsu",
    u"生田絵梨花":"ikuta-erika",
    u"生駒里奈":"ikoma-rina",
    u"伊藤万理華":"itou-marika",
    u"井上小百合":"inoue-sayuri",
    u"衛藤美彩":"etou-misa",
    u"川後陽菜":"kawago-hina",
    u"川村真洋":"kawamura-mahiro",
    u"齋藤飛鳥":"saitou-asuka",
    u"斎藤ちはる":"saitou-chiharu",
    u"斉藤優里":"saitou-yuuri",
    u"桜井玲香":"sakurai-reika",
    u"白石麻衣":"shiraishi-mai",
    u"高山一実":"takayama-kazumi",
    u"中田花奈":"nakada-kana",
    u"中元日芽香":"nakamoto-himeka",
    u"西野七瀬":"nishino-nanase",
    u"能條愛未":"noujou-ami",
    u"橋本奈々未":"hashimoto-nanami",
    u"樋口日奈":"higuchi-hina",
    u"星野みなみ":"hoshino-minami",
    u"松村沙友理":"matsumura-sayuri",
    u"若月佑美":"wakatsuki-yumi",
    u"和田まあや":"wada-maaya",
    u"伊藤かりん":"itou-karin",
    u"伊藤純奈":"itou-junna",
    u"北野日奈子":"kitano-hinako",
    u"相楽伊織":"sagara-iori",
    u"佐々木琴子":"sasaki-kotoko",
    u"新内眞衣":"shinuchi-mai",
    u"鈴木絢音":"suzuki-ayane",
    u"寺田蘭世":"terada-ranze",
    u"堀未央奈":"hori-miona",
    u"山崎怜奈":"yamazaki-rena",
    u"渡辺みり愛":"watanabe-miria",
    u"伊藤理々杏":"itou-riria",
    u"岩本蓮加":"iwamoto-renka",
    u"梅澤美波":"umezawa-minami",
    u"大園桃子":"oozono-momoko",
    u"久保史緒里":"kubo-shiori",
    u"阪口珠美":"sakaguchi-tamami",
    u"佐藤楓":"satou-kaede",
    u"中村麗乃":"nakamura-reno",
    u"向井葉月":"mukai-hazuki",
    u"山下美月":"yamashita-mizuki",
    u"吉田綾乃クリスティー":"yoshida-ayano-christie",
    u"与田祐希":"yoda-yuuki",
    u"３期生":"sankisei",
    u"運営スタッフ":"unei-sutaffu",
    u"administrator":"unei-sutaffu",
    u"スタッフブログ":"unei-sutaffu",
    u"研究生":"kenkyuusei"
}

getAll = []


@asyncio.coroutine
def pageget(url):

    with aiohttp.ClientSession() as session:
        with aiohttp.Timeout(5):
            response = yield from session.get(url,headers=headers)
            try:
                data = yield from response.text(encoding="utf-8",errors='ignore')

                block = re.search(r'''<div id="container">([\s\S]+?)</div>\s*<\!--▼スケジュール-->''',data).group(1)

                valid = re.findall(r'''<div class="pic"><img src="([^"]+)"[\s\S]+?<h3>([^<]+?)<span class="sub">([^<]+?)</span></h3>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<dd>([^<]+?)</dd>[\s\S]+?<div class="status">([\s\S]+)''',block)

                valid = valid[0]

                portrait = re.sub(r'\?\w+$','',valid[0])
                name = re.sub(r' ','',valid[1])
                kana = valid[2][1:-1]
                birthdate = valid[3]
                bloodtype = valid[4]
                constellation =  valid[5]
                height = valid[6]
                status = re.sub(r'<[^>]+?>'," ",valid[7])
                status = re.sub(r'^\s*',"",status)
                status = re.sub(r'\s*$',"",status)
                status = re.sub(r'\s+'," ",status)

                detail = collections.OrderedDict()    
                detail["name"] = name
                detail["kana"] = kana
                detail["rome"] = membersdict[name]
                detail["birthdate"] = birthdate
                detail["bloodtype"] = bloodtype
                detail["constellation"] = constellation
                detail["height"] = height
                detail["status"] = status
                detail["portrait"] = portrait
                detail["link"] = url
                    
                getAll.append(detail)

            except BaseException as e:
                print (e)
                return


def getlist():
    url = "http://www.nogizaka46.com/smph/member/"
    
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req) 

    data = response.read().decode('unicode_escape')
    
    listblock = re.search(r'''<div class="main">([\s\S]+)</div><\!--member end-->''',data).group(1)
    
    urllist = re.findall(r'''\./detail/\w+\.php''',listblock)
    
    back = []  

    for line in urllist:
        back.append("http://www.nogizaka46.com/smph/member"+line[1:])
        
    return back

starttime=datetime.datetime.now()

# urllist = getlist()

urllist = [u'http://www.nogizaka46.com/smph/member/detail/akimotomanatsu.php',
 u'http://www.nogizaka46.com/smph/member/detail/ikutaerika.php',
 u'http://www.nogizaka46.com/smph/member/detail/ikomarina.php',
 u'http://www.nogizaka46.com/smph/member/detail/itoukarin.php',
 u'http://www.nogizaka46.com/smph/member/detail/itoujunna.php',
 u'http://www.nogizaka46.com/smph/member/detail/itoumarika.php',
 u'http://www.nogizaka46.com/smph/member/detail/inouesayuri.php',
 u'http://www.nogizaka46.com/smph/member/detail/etoumisa.php',
 u'http://www.nogizaka46.com/smph/member/detail/kawagohina.php',
 u'http://www.nogizaka46.com/smph/member/detail/kawamuramahiro.php',
 u'http://www.nogizaka46.com/smph/member/detail/kitanohinako.php',
 u'http://www.nogizaka46.com/smph/member/detail/saitouasuka.php',
 u'http://www.nogizaka46.com/smph/member/detail/saitouchiharu.php',
 u'http://www.nogizaka46.com/smph/member/detail/saitouyuuri.php',
 u'http://www.nogizaka46.com/smph/member/detail/sagaraiori.php',
 u'http://www.nogizaka46.com/smph/member/detail/sakuraireika.php',
 u'http://www.nogizaka46.com/smph/member/detail/sasakikotoko.php',
 u'http://www.nogizaka46.com/smph/member/detail/shiraishimai.php',
 u'http://www.nogizaka46.com/smph/member/detail/shinuchimai.php',
 u'http://www.nogizaka46.com/smph/member/detail/suzukiayane.php',
 u'http://www.nogizaka46.com/smph/member/detail/takayamakazumi.php',
 u'http://www.nogizaka46.com/smph/member/detail/teradaranze.php',
 u'http://www.nogizaka46.com/smph/member/detail/nakadakana.php',
 u'http://www.nogizaka46.com/smph/member/detail/nakamotohimeka.php',
 u'http://www.nogizaka46.com/smph/member/detail/nishinonanase.php',
 u'http://www.nogizaka46.com/smph/member/detail/noujouami.php',
 u'http://www.nogizaka46.com/smph/member/detail/higuchihina.php',
 u'http://www.nogizaka46.com/smph/member/detail/hoshinominami.php',
 u'http://www.nogizaka46.com/smph/member/detail/horimiona.php',
 u'http://www.nogizaka46.com/smph/member/detail/matsumurasayuri.php',
 u'http://www.nogizaka46.com/smph/member/detail/yamazakirena.php',
 u'http://www.nogizaka46.com/smph/member/detail/wakatsukiyumi.php',
 u'http://www.nogizaka46.com/smph/member/detail/watanabemiria.php',
 u'http://www.nogizaka46.com/smph/member/detail/wadamaaya.php',
 u'http://www.nogizaka46.com/smph/member/detail/itouriria.php',
 u'http://www.nogizaka46.com/smph/member/detail/iwamotorenka.php',
 u'http://www.nogizaka46.com/smph/member/detail/umezawaminami.php',
 u'http://www.nogizaka46.com/smph/member/detail/oozonomomoko.php',
 u'http://www.nogizaka46.com/smph/member/detail/kuboshiori.php',
 u'http://www.nogizaka46.com/smph/member/detail/sakaguchitamami.php',
 u'http://www.nogizaka46.com/smph/member/detail/satoukaede.php',
 u'http://www.nogizaka46.com/smph/member/detail/nakamurareno.php',
 u'http://www.nogizaka46.com/smph/member/detail/mukaihazuki.php',
 u'http://www.nogizaka46.com/smph/member/detail/yamashitamizuki.php',
 u'http://www.nogizaka46.com/smph/member/detail/yoshidaayanochristie.php',
 u'http://www.nogizaka46.com/smph/member/detail/yodayuuki.php']


# print(urllist)


loop = asyncio.get_event_loop()

tasks = []
for i in range(len(urllist)):
    task = asyncio.async(pageget(urllist[i]))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))

sortedlist = sorted(getAll, key = operator.itemgetter('kana') ,reverse=False)

f = open("allmembers.json", 'w')
f.write(json.dumps(sortedlist,ensure_ascii=False,sort_keys=False,indent=4))
f.close()

executetime=datetime.datetime.now()-starttime

print(str(executetime.seconds+executetime.microseconds/1000000)+"ms")