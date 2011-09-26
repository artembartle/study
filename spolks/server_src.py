#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by bartle on 2011-09-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import socket


def main():
    text_file = open("server.py", "r")
    data = text_file.read()
    text_file.close()
    HOST = ''           
    PORT = 1025
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while 1:
        conn.send(data)
    
    conn.close()


if __name__ == '__main__':
	main()

