import requests
import json
import numpy as np
import re

def g(uid:int):
    
    url="https://api.bilibili.com/x/relation/followings?vmid=%d&pn=%d&ps=50&order=desc&order_type=attention&jsonp=jsonp"# % (UID, Page Number)    
    infos=[]#输出的关注列表
    
    for i in range(1,6):
        html=requests.get(url%(uid,i))#爬到单页列表的网页
        if html.status_code!=200:
            print("GET ERROR!")# 错误信息
        text=html.text#解析
        dic=json.loads(text)#后端接口
        if dic['code']==-400:
            break
        list=dic['data']['list']#字典抓取关注列表
        for person in list:#抓取关键内容
            info={}
            info['mid']=person['mid']
            info['uname']=person['uname']
            infos.append(info)
    return infos

#声明
print("由于站点限制只能访问250个关注,所以统计结果会有误差")
leurl="https://api.bilibili.com/x/space/acc/info?mid=%d&token=&platform=web&jsonp=jsonp"
fourl="https://api.bilibili.com/x/relation/stat?vmid=%d&jsonp=jsonp"

header={
    'cookie': "buvid3=ACA122F5-52B1-6E10-619C-E928D5D13F2010238infoc; i-wanna-go-back=-1; _uuid=983939CD-25D7-3C9E-EE106-EBB991027963196527infoc; buvid_fp_plain=undefined; DedeUserID=436602265; DedeUserID__ckMd5=47cb6e5b799f0cc3; rpdid=|(k||)uY)kkR0J'uYYul)mllR; hit-dyn-v2=1; LIVE_BUVID=AUTO3516615919963528; nostalgia_conf=-1; CURRENT_BLACKGAP=0; b_ut=5; b_nut=100; buvid4=2D7F4F2D-59C8-C4F9-4CEC-D821D5FAB0C908031-022082716-OhPZT1K9L8%2FRxGrQIjMnhg%3D%3D; CURRENT_QUALITY=80; bp_article_offset_436602265=713301060532305900; is-2022-channel=1; SESSDATA=f2ecfcc2%2C1681140374%2Cb3223%2Aa1; bili_jct=94af350c870a181161ca3bfe4597b045; fingerprint=a5cd0c9b6e1c5db237324866c1f48bf6; PVID=5; sid=6uhl4ja0; b_lsid=1072838109_183D06B8780; bp_video_offset_436602265=716383386761953300; innersign=1; CURRENT_FNVAL=4048; buvid_fp=a5cd0c9b6e1c5db237324866c1f48bf6",
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"
}

#输入并处理uid
uid1=input("请输入要比对的第一个uid:")
g1=g(int(uid1))
uid2=input("请输入要比对的第二个uid:")
g2=g(int(uid2))

#uid取交集，提取up名称
C=np.array(g1)[np.in1d(g1,g2)]

if (len(C)==0):
    print("很遗憾,你们没有共同关注的up主")
else:
    print("你们的关注列表如下：")
    for each in C:
        print("uid:",each['mid']," 昵称:",each['uname'],end=" ")
        le=requests.get(leurl%int(each['mid']),headers=header)
        level=re.findall(r'"level":(.*?),',le.text)
        print("level:",level[0],end=" ")
        fo=requests.get(fourl%int(each['mid']))
        foer=re.findall(r'"follower":(.*?)}',fo.text)
        print("粉丝数:",foer[0])
input()
