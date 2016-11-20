import socket
import sys

sock = socket.socket()

sock.connect(('localhost', 9090))

token = ' '.join(sys.argv[1:]) or 'aaa'
sock.send(token)

print ('Can_drop_garbage = not(Can_drop_garbage)')
sock.close()
