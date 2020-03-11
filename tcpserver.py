"""
server.py
"""
from socket import *
from time import ctime
import threading
import time


def server(ho, po):
    HOST = ho
    PORT = po
    BUFSIZE = 4096
    ADDR = (HOST, PORT)
    tcpServer = socket(AF_INET, SOCK_STREAM)
    tcpServer.bind(ADDR)
    tcpServer.listen(10)

    while True:
        #print('等待连接...')
        tcpClient, addr = tcpServer.accept()
        print(addr)

        while True:
            data = tcpClient.recv(BUFSIZE)
            if not data:
                #print('---------')
                break

            print(data.decode())
            buf = '[' + ctime() + ']' + data.decode()
            tcpClient.send(buf.encode())

        tcpClient.close()
    tcpServer.close()


def send_msg(string, host, port):
    s = socket()
    s.connect((host, port))
    s.send(string.encode())
    s.close()


if __name__ == "__main__":
    task = threading.Thread(target=server, args=('',13000,))
    task.start()
    ho = '127.0.0.1'
    po = 13001
    time.sleep(0.5)
    while (True):
        cmd = input()
        send_msg(cmd, ho, po)
