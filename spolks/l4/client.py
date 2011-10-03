#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by bartle on 2011-09-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import socket
import os.path


def main():
    HOST = ''
    PORT = 1052
    buf_size = 1024
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
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
    bytes_left = file_size
    while True:
        buf = s.recv(buf_size)
        s.send(repr(len(buf)))
        rand = s.recv(1024, socket.MSG_OOB)
        print rand
        if buf == '':
            break
        else:
            bytes_left -= len(buf)
            print "Left %d bytes" % bytes_left
            recv_file.write(buf)
    
    recv_file.close()
    s.close()


if __name__ == '__main__':
	main()

