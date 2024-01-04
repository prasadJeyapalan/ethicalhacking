#!/bin/python3

import socket
from datetime import datetime

ip = '127.0.0.1'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))
