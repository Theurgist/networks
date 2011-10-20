#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

from socket import *
import time

def srvWaitForConnect(Sock):
    #Waiting for incoming prey's client connection 
    Sock.setsockopt (SOL_SOCKET, SO_REUSEADDR, True)
    Sock.bind (('', 9000))
    Sock.listen (1)
    client, addr = Sock.accept ()
    print "connected: " + str (addr)
    client.send ("hello")
    return client, addr

def srvMainLoop(client, addr, bDoWeNeedTerminalPrint = False, sLogPath = "distant_events.log"):
    #Entry point for infinite loop
    fileLog = open (sLogPath, "w")
    
    while True:
        # Receive message from client, then send reply
        rec = client.recv (5)
        
        if rec == "end  ":
            # Send reply
            client.send ("end  ")
            return
        else:
            LogEntry = str (addr) + " > " + str (rec)
            if bDoWeNeedTerminalPrint:
                print LogEntry
            print >> fileLog, LogEntry            
            # Send reply
            try:
                client.send ("ok   ")
            except IOError:
                print "connection closed"
                client.close ()
            
    fileLog.close()

# Our main() function :)
def StartServer():
    #Socket initialization
    s = socket (AF_INET, SOCK_STREAM)
    client, addr = srvWaitForConnect(s)
    srvMainLoop(client, addr, True)

    
    s.shutdown (SHUT_RDWR)
    s.close ()
    del s
    
# Application entry point
if __name__ == '__main__':
    StartServer()