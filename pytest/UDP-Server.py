#coding=utf-8
'''
Created on 2014年3月4日

@author: Derek Xie
'''
def server():
    import socket
    address = ('127.0.0.1', 10141)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(address)
    while True:
        data, addr = s.recvfrom(2048)
        print "received:", data, "from", addr
    s.close()

if __name__ == '__main__':
    server()