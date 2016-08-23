#!/usr/bin/python
# socket_client.py

import socket
import sys
import os


def socket_send(command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 1000))
    sock.send(command)
    result = sock.recv(2048)
    sock.close()
    return result


if __name__ == '__main__':
    a = ' '.join(sys.argv[1:])
    a = os.getcwd() + '#*#*#' + a
    print(socket_send(a))
