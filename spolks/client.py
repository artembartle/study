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
    PORT = 1026
    buf_size = 1024
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    length_str = s.recv(1024)
    print repr(length_str)
    s.sendall("ok")
    length = int(length_str)
    incoming = open("2.py", "wa")

    while length:
        try:
            print length
            chunk = s.recv(min(buf_size, length))
            print repr(chunk)
        except socket.error, e:
            print "Error receiving data: %s" % e
        else:    
            incoming.write(chunk)
            length -= len(chunk)
        
    incoming.close()    
    s.close()



if __name__ == '__main__':
	main()

