import socket
import subprocess

sock = socket.socket()

sock.bind(('', 9090))

sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    subprocess.call('python rabbit_emitter_to_cloud.py {}'.format(data), shell=True)


conn.close()
