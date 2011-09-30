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
    PORT = 1051
    buf_size = 1024
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    message = s.recv(1024) # [size_of_file] + ' ' + [file_name]
    message_list = message.split(' ')
    file_name = 'incoming_' + message_list[1]
    file_size = message_list[0]
    
    if os.path.isfile(file_name):
        i = 0
        while os.path.isfile(file_name):
            file_name = str(i) + file_name
            i += 1
            
    recv_file = open(file_name, "a")
    s.send("ok")
    while True:
        buf = s.recv(buf_size)
        if buf == '':
            break
        else:
            recv_file.write(buf)
    
    recv_file.close()
    s.close()


if __name__ == '__main__':
	main()

