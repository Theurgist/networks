#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

from socket import *
import time
import random 

def cliConnect(Sock, IP, Port):
    #Try to connect to hunter's server
    bConnected = False
  # For counting of unsuccessful attempts of connection
  # (for example: when server is not running on given 'ServDest')
    nConnectAttempts = 0
    while not bConnected:
        try:
            Sock.connect((IP, Port))
            bConnected = True
            print "Connected! (Connection attempts used:%i)" % nConnectAttempts;
        except IOError as e:
            nConnectAttempts = nConnectAttempts + 1
            time.sleep (2)
            print "Not connected =( (Connection attempts used:%i)" % nConnectAttempts;

# Application entry point
if __name__ == '__main__':
    # Socket initialization
    s = socket(AF_INET, SOCK_STREAM)
    cliConnect(s, '195.19.35.160', 9000)

    tm = s.recv(5)

    while True:
        #print "*"
        d = random.randrange (0, 10)
        print "send: " + "msg:" + str (d)
        s.send ("msg:" + str (d));
        tm = s.recv(5)
        if tm == "end":
            print "stop."
        else:
            print "responce: " + tm
        time.sleep (random.randrange (1, 4))
    #s.send ("end  ");
    s.close()