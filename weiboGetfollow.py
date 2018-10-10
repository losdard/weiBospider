# -*- coding: utf-8 -*-
import json
import weiboGetproxy
import weibofunction
import time

#设置代理IP
proxy_addr=weiboGetproxy.get_proxy('http://www.xicidaili.com/nn')

#获取微博用户关注明细
def get_followers(id):
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_' + id
    data= weibofunction.use_proxy(url, proxy_addr[4])
    content=json.loads(data).get('data')
    cards=content.get('cards')
    pList=[]
    if len(cards)>1:
        for c in range(len(cards)-1):
            linkIndex=cards[c].get('card_group')[0].get('scheme').replace('https://m.weibo.cn/p/index', 'https://m.weibo.cn/api/container/getIndex')
            data= weibofunction.use_proxy(linkIndex, proxy_addr[3])
            content = json.loads(data).get('data')
            infocards = content.get('cards')
            if len(infocards)>0:
                for f in range(len(infocards)):
                    pIndex=infocards[f].get('card_group')
                    for s in range(len(pIndex)):
                        if pIndex[s].get('card_type')<42:
                            pList=weibofunction.get_info(pIndex[s])
                            #print(pList)
                            time.sleep(1)
                            weibofunction.insertData("insert into userTable(weiBoid, userName, infoName, urlAdress, userFollower, userFans, updateCount) " +
                                                     "values("+str(pList[3])+",'"+str(pList[1])+"','"+str(pList[2])+"','"+str(pList[0])+"',"+str(pList[4])+","+str(pList[5])+",0)")
                            #with open(followfile, 'a', encoding='utf-8') as fh:
                                #fh.write(str(pList[0]) + ',' + str(pList[1]) + ',' + str(pList[2]) + ',' + str(pList[3]) + ',' + str(pList[4]) + ',' + str(pList[5]) + '\n')
        pIndex=cards[len(cards)-1].get('card_group')
        if len(pIndex)>0:
            for p in range(len(pIndex)):
                pList=weibofunction.get_info(pIndex[p])
                #print(pList)
                time.sleep(1)
                weibofunction.insertData(
                    "insert into userTable(weiBoid, userName, infoName, urlAdress, userFollower, userFans, updateCount) " +
                    "values(" + str(pList[3]) + ",'" + str(pList[1]) + "','" + str(pList[2]) + "','" + str(
                        pList[0]) + "'," + str(pList[4]) + "," + str(pList[5]) + ",0)")
                #with open(followfile, 'a', encoding='utf-8') as fh:
                    #fh.write(str(pList[0])+','+str(pList[1])+','+str(pList[2])+','+str(pList[3])+','+str(pList[4])+','+str(pList[5])+'\n')
    else:
        pIndex=cards[0].get('card_group')
        if len(pIndex)>0:
            for p in range(len(pIndex)):
                pList=weibofunction.get_info(pIndex[p])
                #print(pList)
                time.sleep(1)
                weibofunction.insertData(
                    "insert into userTable(weiBoid, userName, infoName, urlAdress, userFollower, userFans, updateCount) " +
                    "values(" + str(pList[3]) + ",'" + str(pList[1]) + "','" + str(pList[2]) + "','" + str(
                        pList[0]) + "'," + str(pList[4]) + "," + str(pList[5]) + ",0)")

