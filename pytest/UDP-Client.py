#coding=utf-8
'''
Created on 2014年3月4日

@author: Derek Xie
'''
def client():
    import socket
    address = ('127.0.0.1', 10141)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = raw_input()
        if not message:
            break
        s.sendto(message, address)
    s.close()

if __name__ == '__main__':
    client()