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
    PORT = 1049
    buf_size = 1024
    

    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
    icmp_socket.connect((HOST, PORT))


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    length_str = s.recv(1024)
    print length_str
    s.sendall("ok")
    length = int(length_str)
    incoming = open("2.c", "w")
    incoming.close()

    while length:
        try:
            print length
	    incoming = open("2.c", "a")
            chunk = s.recv(min(buf_size, length))
            print (icmp_socket.recv(32))
	    print chunk
        except socket.error, e:
            print "Error receiving data: %s" % e
	except socket.timeout, e:
	    print "Connection timeout: %s" % e
        else:    
            incoming.write(chunk)
	    incoming.close()
            length -= len(chunk)
        
    s.close()
    icmp_socket.close()


if __name__ == '__main__':
	main()

