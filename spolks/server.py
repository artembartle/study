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
    send_file = open("1.c", "r")
    data = send_file.read()
    send_file.close()
    data_size = len(data)
    print data_size

    HOST = ''           
    PORT = 1049
    buf_size = 1024
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:    
        conn.send(repr(data_size))
        if conn.recv(2) == "ok":
            while data_size:
                print data_size
                buf_size = min(buf_size, data_size)
		buf = data[:buf_size]
                try:
                    print conn.send(buf)
                    print buf
		except socket.herror, e:
		    print "sdfsd"	
		except socket.gaierror, e:
		    print "gsdfgdf"	
                except socket.error, e:
                    print "Error sending data: %s" % e
		except socket.timeout, e:
		    print "Connection timeout: %s" % e
                else:
		    data =  data[buf_size:]
                    data_size -= buf_size
		    time.sleep(1)
	    break
    
    conn.close()


if __name__ == '__main__':
	main()

