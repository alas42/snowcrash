#!/usr/bin/python3
import socket
import sys
import math
import base64
import codecs
import zlib

#Fixed variables for connection and discussions
port = 5151
ip = "10.0.0.84"
client = socket.socket()

#Socket connection
def joinserver():
    client.connect((ip, port))

def main():
    joinserver()
    
main()