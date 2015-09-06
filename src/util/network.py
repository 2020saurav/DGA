import socket
import sys
sys.path.append('../../')

from config.networkParams import *

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

def sendAndGetResponseFromIP(IP, port, message):
    s = socket.socket()
    s.connect((IP, port))
    s.send(messageLength(message))
    s.send(message)
    respLen = int(s.recv(MESSAGE_LENGTH_DIGITS))
    resp = s.recv(respLen)
    s.close()
    return resp

def sendAndGetResponse(sock, message):
    sock.send(messageLength(message))
    sock.send(message)
    respLen = int(sock.recv(MESSAGE_LENGTH_DIGITS))
    resp = sock.recv(respLen)
    return resp
