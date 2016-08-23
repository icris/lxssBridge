#!/usr/bin/python
# socket_client.py

import socket
import sys
import os


def socket_send(command):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 1000))
    sock.send(command)
    result = sock.recv(2048)
    sock.close()
    return result


if __name__ == '__main__':
    cmd = os.getcwd() + '#*#*#' + ' '.join(sys.argv[1:])
    print(socket_send(cmd))
