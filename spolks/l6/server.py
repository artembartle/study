#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by bartle on 2011-09-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import socket
import os.path
import time

def main():
    
    HOST = ''           
    PORT = 1053
    FILE_NAME = "1.c"
    buf_size = 1024
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    send_file = open(FILE_NAME, "r")
    file_size = os.path.getsize(FILE_NAME)
    
    while True:
        message, addr = s.recvfrom(1024)
        if message == "Hello":
            s.sendto(str(file_size) + ' ' + FILE_NAME, addr)
            while file_size:
                buf_size = min(buf_size, file_size)
                buf = send_file.read(buf_size)
                bytes_sended = s.sendto(buf, addr)
                message, addr = s.recvfrom(1024)
                bytes_recieved = int(message)
                if bytes_sended != buf_size or bytes_sended != bytes_recieved:
                    print "error conn.send(buf) != buf_size:"
                    send_file.seek(-buf_size, 1)
                    time.sleep(0.5)
                else:
                    file_size -= buf_size
                    print "Left %d bytes" % file_size
                    time.sleep(0.5)
   
    s.close()
    send_file.close()

if __name__ == '__main__':
	main()

