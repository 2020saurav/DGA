'''
Network call handler of slave server
'''

from socket import *
import sys
import thread
sys.path.append('../../config')
sys.path.append('../util')

from networkParams import *
import network
import main

Slave = main.Main()

def handler(sc, address):
    messageLength = int(sc.recv(MESSAGE_LENGTH_DIGITS))
    message = sc.recv(messageLength)
    words = message.split(MESSAGE_DELIMITER)

    if words[0] == 'SERVERINFO':
        Slave.saveServerInfo(message)
    else:
        network.send(sc, MESSAGE_UNRECOGNIZED)

    sc.close()

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST_IP, 2021)) # TODO change to HOST_PORT
    s.listen(MAX_BACKLOG_CONN)
    while True:
        sc, address = s.accept()
        thread.start_new_thread(handler, (sc, address))
    s.close()
