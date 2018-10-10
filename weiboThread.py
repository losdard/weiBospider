#coding:utf-8
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,target,args):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.target = target
        self.args=args
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        self.target(self.args)