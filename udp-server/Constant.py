#coding=utf-8
'''
Created on 2014年3月5日

@author: Derek Xie
类定义：设置公共数据
'''

class Constant:
    '''
    classdocs
    '''
    beginStr = "Derek+"#字符串开头标识
    endStr = "+Xie"#字符串结尾标识
    port = 8088#服务端监听的端口
    ip = "192.168.1.111"#服务端的ip
    returnResoutOk = "O"#返回成功数据标识"WordGet"
    returnResoutNull = "N"#返回空数据标识"WordNull"
    returnResoutError = "E"#返回数据包错误数据标识“UDPPackagesError”
    
    def __init__(selfparams):
        '''
        Constructor
        '''
        