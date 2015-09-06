'''
Network call handler of master server
'''

import main
import thread
import src.util.network
from socket import *
from config.networkParams import *

Master = main.Main()

def handler(sc, address):
    messageLength = int(sc.recv(MESSAGE_LENGTH_DIGITS))
    message = sc.recv(messageLength)
    words = message.split(MESSAGE_DELIMITER)

    if words[0] == 'GETSERVERINFO':
        response = Master.getServerListNetString()
        network.send(sc, response)
    elif words[0] == 'INPUT':
        Master.processInput(message)
    elif words[0] == 'HEARTBEAT':
        Master.recordHeartBeat(message)
    elif words[0] == 'PING':
        Master.recordPing(message)
        network.send(sc, 'PONG')
    elif words[0] == 'PONG':
        Master.recordPong(message)
    elif words[0] == 'PARTIALRESULT':
        Master.processPartialResult(message)
    elif words[0] == 'JOBCOMPLETE':
        Master.recordJobCompleteNotification(message)
    else:
        Master.unrecognizedMessage(message)

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
