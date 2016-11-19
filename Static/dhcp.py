#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('10.212.2.123', 666))
sock.send('Ivan Potyutkov P456HM Ok')

data = sock.recv(1024)
sock.close()

print data
