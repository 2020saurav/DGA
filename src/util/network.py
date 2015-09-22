import socket
from config.networkParams import *
from config.messageHeads import *
from config.host import *
import src.util.logger as logger

log = logger.getLogger("Network-Util")

def messageLength(message):
    if len(message) >= 10**MESSAGE_LENGTH_DIGITS:
        log.error("Message length exceeds network limit", exc_info=True)
    return str(('%0'+str(MESSAGE_LENGTH_DIGITS)+'d')%len(message))

def sendToIP(IP, port, message):
    s = socket.socket()
    s.connect((IP, port))
    s.send(messageLength(message))
    s.send(message)
    log.info("Message sent to IP " + IP + ':' + str(port))
    s.close()

def send(sock, message):
    sock.send(messageLength(message))
    sock.send(message)
    log.info("Message sent to socket")

def sendAndGetResponseFromIP(IP, port, message):
    s = socket.socket()
    s.connect((IP, port))
    s.send(messageLength(message))
    s.send(message)
    log.info("Message sent to IP " + IP + ':' + str(port))
    respLen = int(s.recv(MESSAGE_LENGTH_DIGITS))
    resp = s.recv(respLen)
    log.info("Response received. Length: " + str(len(resp)))
    s.close()
    return resp

def sendAndGetResponse(sock, message):
    sock.send(messageLength(message))
    sock.send(message)
    log.info("Message sent to socket")
    respLen = int(sock.recv(MESSAGE_LENGTH_DIGITS))
    resp = sock.recv(respLen)
    log.info("Response received. Length: " + str(len(resp)))
    return resp

def sendPingForAliveTest(server):
    log.info('Sending ping to server ' + server.ID + ' ' + server.IP + ':' + str(server.port))
    message = PING + MESSAGE_DELIMITER + HOST_ID
    try:
        # TODO add timeout here
        response = sendAndGetResponseFromIP(server.IP, server.port, message)
        log.info('PING response received from server ' + server.ID + ': '+ response)
        return True
    except:
        response = None
        log.error('No PING response from server ' + server.ID + '. Marking it dead.', exc_info=True)
        return False
