'''
Network call handler of slave server
'''

from socket import *
import thread
from config.networkParams import *
from config.host import *
import src.util.network as network
import main

Slave = main.Main()

def handler(sc, address):
    messageLength = int(sc.recv(MESSAGE_LENGTH_DIGITS))
    message = sc.recv(messageLength)
    words = message.split(MESSAGE_DELIMITER)

    if words[0] == 'SERVERINFO':
        Slave.saveServerInfo(message)
    elif words[0] == 'GRAPH':
        Slave.saveGraph(message)
    elif words[0] == 'PUSHTASK':
        Slave.pushTaskToQueue(message)
    elif words[0] == 'POPPEDTASK':
        Slave.receivePoppedTask(message)
    elif words[0] == 'STARTPROCESSING':
        Slave.startProcessing(message)
    elif words[0] == 'REQUESTTASK':
        response = Slave.grantTask(message)
        network.send(sc, response)
    elif words[0] == 'SENDPARTIALRESULT':
        response = Slave.getPartialResult(message)
        network.send(sc, response)
    elif words[0] == 'HASHCHECK':
        response = Slave.checkHash(message)
        network.send(sc, response)
    elif words[0] == 'HASHRESPONSE':
        Slave.processHashResponse(message)
    elif words[0] == 'PING':
        Slave.recordPing(message)
        network.send(sc, 'PONG')
    else:
        Slave.unrecognizedMessage(message)

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
