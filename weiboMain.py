# -*- coding: utf-8 -*-

import urllib.request
import threading
import time
import requests
import json
import weiboGetproxy
import weiboThread
import weibofunction
import weiboGetfollow
from PyQt5 import *

#定义要爬取的微博大V的微博ID
id=['2143999165','1707683373','2173878502']
#hfans='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_'+id
#hfollowers='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_'+id
#ipath = 'E:/weibo/' + id + '/'
#file = ipath + id + ".txt"
#fansfile = ipath + id + "_fans.txt"
#followfile = ipath + id + "_follow.txt"
#设置代理IP
proxy_addr=weiboGetproxy.get_proxy('http://www.xicidaili.com/nn')
thread_list = []

def sTartWeibo():
    t=weiboThread.MyThread(weibofunction.unSearch,1)
    t.start()

def SearchFollower(id):
    t=weiboThread.MyThread(weiboGetfollow.get_followers,id)
    t.setDaemon(True)
    thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()


if __name__=="__main__":
    sTartWeibo()
