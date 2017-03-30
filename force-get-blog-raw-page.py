#! /usr/local/bin/python3.4
  
import asyncio
import aiohttp
import re
import os 
import json

base_dir = os.getcwd()

@asyncio.coroutine
def pageget(url):
    part = url.split("/")
    relative_dir = part[3] + "/" + part[5] + "/" + part[6] +"/"
    filename = part[7][:-3] + "html"

    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"}
    with aiohttp.ClientSession() as session:
        with aiohttp.Timeout(5):
            response = yield from session.get(url,headers=headers)
            try:
                data = yield from response.text("utf-8")

                data = re.sub(r'\.\./\.\./\.\./\.\./',"http://blog.nogizaka46.com/",data)

                if os.path.exists(base_dir + relative_dir)==0:
                    os.makedirs(base_dir + relative_dir)

                f = open(base_dir + relative_dir + filename,"w")
                f.write(data)
                f.close()

                return
            except BaseException as e:
                print (e)
                return

f = open('nanami.json','r')
data = f.read()
jsonData = json.loads(data)
urllist = []

for line in jsonData:
    urllist.append(line["url"])

loop = asyncio.get_event_loop()

tasks = []
for url in urllist:
    task = asyncio.async(pageget(url))
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
#print(tasks)