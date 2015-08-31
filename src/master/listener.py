'''
Network call handler of master server
'''

from socket import *
import sys
import thread
sys.path.append('../../config')

from networkParams import *
import responder

def handler(sc, address):
    messageLength = int(sc.recv(MESSAGE_LENGTH_DIGITS))
    message = sc.recv(messageLength)
    words = message.split(MESSAGE_DELIMITER)
    print words
    responder.send(sc, MESSAGE_RECEIPT_SUCCESS)
    sc.close()

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST_IP, HOST_PORT))
    s.listen(MAX_BACKLOG_CONN)
    while True:
        sc, address = s.accept()
        thread.start_new_thread(handler, (sc, address))
    s.close()
