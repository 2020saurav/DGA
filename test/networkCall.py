import socket
import sys
sys.path.append('../config')

from networkParams import *

def messageLength(message):
    return str(('%0'+str(MESSAGE_LENGTH_DIGITS)+'d')%len(message))

def request(IP, port, message):
    s = socket.socket()
    s.connect((IP, port))
    s.send(messageLength(message))
    s.send(message)
    respLen = int(s.recv(MESSAGE_LENGTH_DIGITS))
    resp = s.recv(respLen)
    s.close()
    return resp

if __name__ == '__main__':
    IP = '127.0.0.1'
    port = 2020
    message = "Hello$world"
    response = request(IP, port, message)
    print response
