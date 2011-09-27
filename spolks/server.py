#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by bartle on 2011-09-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import socket
import time


def main():
    send_file = open("server.py", "r")
    data = send_file.read()
    data_size = len(data)
    
    HOST = ''           
    PORT = 1026
    buf_size = 1024
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:    
        conn.send(data_size)
        if conn.recv(2) == "ok":
            while data_size:
                print data_size
                buf_size = min(buf_size, data_size)
                buf = send_file.read(buf_size)
                try:
                    print conn.sendall(repr(buf))
                    print repr(buf)
                except socket.error, e:
                    print "Error sending data: %s" % e
                else:
                    send_file.seek(buf_size, 1)
                    print send_file.tell()
                    data_size -= buf_size
#                    time.sleep(3)
    
    conn.close()
    send_file.close()


if __name__ == '__main__':
	main()

