#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by bartle on 2011-09-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import socket
import os
import time


def main():
    
    HOST = ''           
    PORT = 1051
    FILE_NAME = "1.c"
    buf_size = 1024    
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    
    send_file = open(FILE_NAME, "r")
    file_size = os.path.getsize(FILE_NAME)
    conn.send(str(file_size) + ' ' + FILE_NAME)
    if conn.recv(2) == "ok":
        while file_size:
            buf_size = min(buf_size, file_size)
            buf = send_file.read(buf_size)
            byte_sended = conn.send(buf)
            if byte_sended != buf_size:
                print "error conn.send(buf) != buf_size:"
                send_file.seek(-buf_size, 1)
            else:
                file_size -= buf_size
                time.sleep(0.5)
    
    conn.close()
    s.close()
    send_file.close()

if __name__ == '__main__':
	main()

