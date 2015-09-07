import socket
from config.networkParams import *
import src.util.server as server
import src.util.network as network
from config.host import *

def messageLength(message):
    return str(('%0'+str(MESSAGE_LENGTH_DIGITS)+'d')%len(message))

def testMasterServerList(IP, port):
    message = 'GETSERVERINFO'
    response = network.sendAndGetResponseFromIP(IP, port, message)
    servers = server.netStringToServerList(response)
    assert len(servers) == 4
    assert servers[0].role == "master"
    print "Master Server List Test Passed"

def testHelloWorld(IP, port):
    message = "Hello$world"
    response = network.sendToIP(IP, port, message)
    print 'Hello World Test Passed'

def testPingPong(IP, port):
    message = "PING"
    response = network.sendAndGetResponseFromIP(IP, port, message)
    assert response == 'PONG'
    print "Ping Test Passed"

if __name__ == '__main__':
    IP = HOST_IP
    port = HOST_PORT
    testHelloWorld(IP, port)
    testMasterServerList(IP, port)
    testPingPong(IP, port)
