#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by bartle on 2011-09-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import socket
import os
import errno
import signal
import fcntl
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bytes_recieved = 0

def handler(signum, frame):
    print "SIGURG!!!"
    try:
        oob_data = s.recv(1, socket.MSG_OOB)
    except socket.error, why:
        print os.strerror(why[0]) 
    else:
        print "oob_data: %s" % oob_data
        print "Recieved %d bytes" % bytes_recieved
        time.sleep(0.5)


def main():
    HOST = ''
    PORT = 1053
    buf_size = 1024
    global bytes_recieved
    
    s.connect((HOST, PORT))
    signal.signal(signal.SIGURG, handler)
    fcntl.fcntl(s.fileno(), fcntl.F_SETOWN, os.getpid())
    
    message = s.recv(1024) # [size_of_file] + ' ' + [file_name]
    message_list = message.split(' ')
    file_name = 'incoming_' + message_list[1]
    file_size = int(message_list[0])
    
    if os.path.isfile(file_name):
        i = 0
        while os.path.isfile(str(i) + file_name):
            i += 1
        file_name = str(i) + file_name
            
    recv_file = open(file_name, "a")
    s.send("ok")
    while True:
        try:
            buf = s.recv(buf_size)
        except socket.error, why:
            print os.strerror(why[0]) 
        else:
            if buf == '':
                break
            else:
                s.send(repr(len(buf)))
                recv_file.write(buf)
                bytes_recieved += len(buf)
        
    recv_file.close()
    s.close()


if __name__ == '__main__':
	main()

