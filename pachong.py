import bs4 as b
import urllib
import requests as req
import re
import time

r=req.get("https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010")#获取页面

soup =b.BeautifulSoup(r.text,"html.parser")#截取数据
k=soup.select(".leftNews3")
date=re.findall(r'\[\d+-\d+-\d+\]',r.text)
d=re.findall(r'\[(\d+)-(\d+)-(\d+)\]',r.text)

pre=time.localtime(time.time())
if ((pre.tm_year*10000+pre.tm_mon*100+pre.tm_mday)-int(d[0][0]+d[0][1]+d[0][2])<=0):
    print("你当天有新消息，请记得处理")
elif ((pre.tm_year*10000+pre.tm_mon*100+pre.tm_mday)-int(d[0][0]+d[0][1]+d[0][2])<=0):
    print("你一天内有新消息，请记得处理")
elif ((pre.tm_year*10000+pre.tm_mon*100+pre.tm_mday)-int(d[0][0]+d[0][1]+d[0][2])<=0):
    print("你两天内有新消息，请记得处理")
else:
    print("暂时没有新消息呢")


ju=input('按"1"键查看最近15条通知')#后处理
if (ju=="1"):
    i=0#输出结果
    for div in k:
        content=div.find(name="a").string
        print(content)
        url=div.find(name="a").get('href')
        if (url[0:4]=="http"):
            print(url)
        else:
            print("https://www.bkjx.sdu.edu.cn/"+url)
        print(date[i])
        i+=1
        print("")
input()

