#!/bin/python3
import socket

host = '127.0.0.1'
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## AF_INET is IPV4 and SOCK_STREAM is TCP port

s.connect((host, port))
