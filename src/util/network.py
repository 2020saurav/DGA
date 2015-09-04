import socket
import sys
sys.path.append('../../config')

from networkParams import *

def messageLength(message):
    return str(('%0'+str(MESSAGE_LENGTH_DIGITS)+'d')%len(message))

def sendToIP(IP, port, message):
    s = socket.socket()
    s.connect((IP, port))
    s.send(messageLength(message))
    s.send(message)
    s.close()

def send(sock, message):
    sock.send(messageLength(message))
    sock.send(message)
