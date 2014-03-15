#coding=utf-8
'''
Created on 2014年3月4日

@author: Derek Xie
'''
from socket import *
import codecs
import sys
import time
import Constant
'''
@author: DerekXie
函数功能：获取当前时间，格式为2012-12-12
参数定义：无参数
'''
def ctime():
    timeNum = time.time()
    timeLocal = time.localtime(timeNum)
    timeNow = time.strftime('%Y-%m-%d',timeLocal)
    return timeNow

'''
@author: DerekXie
函数功能：UDP服务器
参数定义：无参数
'''
def dealDatas(data):
    print "Deal the data! "+data
    
'''
@author: DerekXie
函数功能：UDP服务器
参数定义：无参数
'''
def server():
    constant = Constant.Constant()
    PORT = constant.port # arbitrary, just make it match in Android code
    IP = constant.ip # represents any IP address
    
    sock = socket(AF_INET, SOCK_DGRAM) # SOCK_DGRAM means UDP socket
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # make socket reuseable
    sock.bind((IP, PORT))
    print "Waiting..."
    while True:
        print "Waiting for data..."
        data, addr = sock.recvfrom(2048) # 返回的接收的数据，和发送数据的地址以及端口
        print('Received:',data,'from',addr)
        Str = data
        beginStr = constant.beginStr
        endStr = constant.endStr
        dataReturn = constant.returnResoutOk
        if Str.startswith(beginStr) and Str.endswith(endStr):
            print "get the right words!"
            getStr = Str[6:-4]#获取真正传入的信息
            if len(getStr)==0:
                dataReturn = constant.returnResoutNull
                print "the word is null!  Return the Null Mark!"
            else:
                print "go on!   Return the right Mark!"+ctime()
                #处理返回的数据
                dealDatas(getStr)
        else:
            dataReturn = constant.returnResoutError
            print "can not get the UDP Packages!   Return the Error Mark!"
        sock.sendto(('[%s] %s'%(ctime(),dataReturn)).encode('utf8'),addr) #传输处理后的数据，需要写addr，仍然因为是无连接

if __name__ == '__main__':
    server()