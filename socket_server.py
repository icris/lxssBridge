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
            cmd = conn.recv(2048).decode('utf-8').split('#*#*#')
            os.chdir(convert(cmd[0]))
            try:
                result = subprocess.check_output('cmd /C ' + cmd[1])  # or ('powerShell /C ' + cmd[1]) if you prefer
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
        path = os.environ['localAppData'].replace("\\", "/") + '/lxss' + path
    return path


if __name__ == '__main__':
    print('listening...')
    main()
