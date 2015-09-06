import socket
import sys
sys.path.append('../')

from config.networkParams import *
import src.util.server

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

def testMasterServerList(IP, port):
    message = 'GETSERVERINFO'
    response = request(IP, port, message)
    servers = server.netStringToServerList(response)
    assert len(servers) == 4
    assert servers[0].role == "master"
    print "Master Server List Test Passed"

def testHelloWorld(IP, port):
    message = "Hello$world"
    response = request(IP, port, message)
    assert response == 'UNRECOGNIZED'
    print 'Hello World Test Passed'

def testMasterSlaveServer(IP, port):
    message = "TESTMASTERSLAVESERVER"
    response = request(IP, port, message)
    # assert
    print 'Master Slave Server List tested'

if __name__ == '__main__':
    IP = '127.0.0.1'
    port = 2020
    testHelloWorld(IP, port)
    testMasterServerList(IP, port)
    testMasterSlaveServer(IP, port)
