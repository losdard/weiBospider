# -*- coding: utf-8 -*-
import urllib.request
import weiboMain
import weiboSqlconn
import weiboMain
import time

def use_proxy(url,proxy_addr):
    req=urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
    return data

def countDatabase(SqlStr):
    conn = weiboSqlconn.createConnection()
    if not conn:
        raise (NameError, "连接数据库失败")
    else:
        data=weiboSqlconn.queryWeiboID(SqlStr, conn)
    return data

def insertData(SqlStr):
    conn=weiboSqlconn.createConnection()
    if not conn:
        raise (NameError, "连接数据库失败")
    else:
        try:
            #print(SqlStr)
            weiboSqlconn.ExecNonQuery(SqlStr, conn)
            time.sleep(1)
        except Exception as e:
            print(e)
            pass

def unSearch(id):
    idStr = ['2143999165', '1500452444','6158404096']
    weiBOid=countDatabase("select top (5) * from userTable where updatecount=0;")
    for i in range(len(weiBOid)):
        if weiBOid[i] in idStr:
            print("此ID已注销，此线程停止!")
        else:
            weiboMain.SearchFollower(weiBOid[i])

def get_info(pIndex):
    plist = []
    scheme=pIndex.get('scheme')
    desc1=pIndex.get('desc1')
    screen_name=pIndex.get('user').get('screen_name')
    uid=pIndex.get('user').get('id')
    follow_count=pIndex.get('user').get('follow_count')
    followers_count=pIndex.get('user').get('followers_count')
    plist.append(scheme)
    plist.append(screen_name)
    plist.append(desc1)
    plist.append(uid)
    plist.append(follow_count)
    plist.append(followers_count)
    return plist