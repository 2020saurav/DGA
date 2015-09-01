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

def handler(sc, address):
    messageLength = int(sc.recv(MESSAGE_LENGTH_DIGITS))
    message = sc.recv(messageLength)
    words = message.split(MESSAGE_DELIMITER)
    print words
    network.send(sc, MESSAGE_RECEIPT_SUCCESS)
    sc.close()

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    #TODO diff port for slave
    s.bind((HOST_IP, HOST_PORT))
    s.listen(MAX_BACKLOG_CONN)
    while True:
        sc, address = s.accept()
        thread.start_new_thread(handler, (sc, address))
    s.close()
