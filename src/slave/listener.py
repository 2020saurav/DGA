'''
Network call handler of slave server
'''

from socket import *
import thread
from config.networkParams import *
from config.host import *
from config.messageHeads import *
import src.util.network as network
import main

Slave = main.Main()

def handler(sc, address):
    messageLength = int(sc.recv(MESSAGE_LENGTH_DIGITS))
    networkMessage = sc.recv(messageLength)
    words = networkMessage.split(MESSAGE_DELIMITER)
    message = MESSAGE_DELIMITER.join(words[1:])
    messageHead = words[0]

    if messageHead == SERVERINFO:
        Slave.saveServerInfo(message)
    elif messageHead == GRAPH:
        Slave.saveGraph(message)
    elif messageHead == PUSHTASK:
        main.pushTaskToQueue(message)
    elif messageHead == STARTPROCESSING:
        Slave.startProcessing(message)
    elif messageHead == REQUESTTASK:
        response = main.grantTask()
        network.send(sc, response)
    elif messageHead == SENDPARTIALRESULT:
        response = Slave.getPartialResult(message)
        network.send(sc, response)
    elif messageHead == HASHCHECK:
        response = main.checkHash(message)
        network.send(sc, response)
    elif messageHead == PING:
        Slave.recordPing(message)
        network.send(sc, PONG)
    elif messageHead == NETWORKPRIME:
        Slave.saveNetworkPrime(message)
    else:
        Slave.unrecognizedMessage(message)

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
