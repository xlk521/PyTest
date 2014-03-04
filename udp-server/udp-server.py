#coding=utf-8
'''
Created on 2014年3月4日

@author: Derek Xie
'''
from socket import *
def server():
    PORT = 8088 # arbitrary, just make it match in Android code
    IP = "192.168.1.111" # represents any IP address
    
    sock = socket(AF_INET, SOCK_DGRAM) # SOCK_DGRAM means UDP socket
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # make socket reuseable
    sock.bind((IP, PORT))
    
    while True:
        print "Waiting for data..."
        data, addr = sock.recvfrom(1024) # 返回的接收的数据，和发送数据的地址以及端口
#         data = data.decode('utf-8')#将编码格式转换成UTF-8模式
#         udpSerSock.sendto(('[%s] %s'%(ctime(),data)).encode('utf8'),addr) #传输处理后的数据，需要写addr，仍然因为是无连接
        print "received: " + data
        print('Received:',data,'from',addr)
        
if __name__ == '__main__':
    server()