# socket_server.py

import os
import socket
import subprocess
import sys


def main():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 1000))
    sock.listen(5)
    while True:
        try:
            conn, address = sock.accept()
            cmd = conn.recv(2048).decode('utf-8')
            arr = cmd.split('#*#*#')
            os.chdir(convert(arr[0]))
            try:
                result = subprocess.check_output(arr[1])
            except Exception as e:
                result = str(e).encode('utf-8')
            conn.send(result)
            conn.close()
        except KeyboardInterrupt:
            print('exit')
            sys.exit(0)
    sock.close()


def convert(path):
    if path.startswith('/mnt'):
        path = path[5] + ':' + path[6:]
    else:
        path = 'C:/Users/icris/AppData/Local/lxss' + path
    return path


if __name__ == '__main__':
    print('listening...')
    main()
