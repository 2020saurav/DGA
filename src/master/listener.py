'''
Network call handler of master server
'''

import main
import thread
import src.util.network as network
from socket import *
from config.networkParams import *
from config.host import *
from config.messageHeads import *

Master = main.Main()

def handler(sc, address):
    messageLength = int(sc.recv(MESSAGE_LENGTH_DIGITS))
    networkMessage = sc.recv(messageLength)
    words = networkMessage.split(MESSAGE_DELIMITER)
    message = MESSAGE_DELIMITER.join(words[1:])
    messageHead = words[0]

    if messageHead == GETSERVERINFO:
        response = Master.getServerListNetString()
        network.send(sc, response)
    elif messageHead == INPUT:
        Master.processInput(message)
    elif messageHead == HEARTBEAT:
        Master.recordHeartBeat(message)
    elif messageHead == PING:
        Master.recordPing(message)
        network.send(sc, PONG)
    elif messageHead == PARTIALRESULT:
        Master.processPartialResult(message)
    elif messageHead == JOBCOMPLETE:
        Master.recordJobCompleteNotification()
    else:
        Master.unrecognizedMessage(message)

    sc.close()

if __name__ == '__main__':
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST_IP, HOST_PORT))
    print "Listening on " + str(HOST_PORT)
    s.listen(MAX_BACKLOG_CONN)
    while True:
        sc, address = s.accept()
        thread.start_new_thread(handler, (sc, address))
    s.close()
