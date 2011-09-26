#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by bartle on 2011-09-26.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
import socket


def main():
    HOST = ''
    PORT = 1025
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    incoming = open("server_src.py", "w")
    incoming.write(s.recv(1024))
    s.close()
    incoming.close()


if __name__ == '__main__':
	main()

