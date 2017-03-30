# Serving the project "idol"  
Some one-key tools for saving time

### Get official protraits  
***keyakizaka46⊿***  
`python get-keyaki-members-official-portraits.py`  

***nogizaka46⊿***  
`python get-nogi-members-official-portraits.py`  

Coding with python 2.7, standard library only, no additional module required.

### Get member's blog list 
***nogizaka46⊿***  
`python get-nogi-members-all-blog-list.py`  

You can set the time limit, default is getting from the earlist blog.  
You can also set the specific member, just change the dict's key.  

Coding with python 2.7, standard library only, no additional module required.  

### Download blog page
***nogizaka46⊿***  
`python3 force-get-blog-raw-page.py`  
Relying on the url list gotten by prev script.  
Storing like official website's php url definition.  

Coding with python 3.4, upwards compatible, required module "asyncio", "aiohttp".  
**Using async to make requests, care with your ip address because of huge concurrency**

### Sample  
hashimoto nanami's "all" blog list are uploaded  
hashimoto nanami's "completed" blog pages are uploaded (will be closed on 31st March, 2017)   
the official website(smph)'s unknown bug causing one blog lost.  
Recommand idolx46.top/nanami to get a better reading experience :)     