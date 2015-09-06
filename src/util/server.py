import sys
sys.path.append('../../')

from config.networkParams import *

class Server:
    def __init__(self, ID, IP, port, role, alive):
        self.ID = ID
        self.IP = IP
        self.port = port
        self.role = role
        self.alive = alive
    
    def toNetString(self):
        netString = ''
        netString += (self.ID + MESSAGE_DELIMITER)
        netString += (self.IP + MESSAGE_DELIMITER)
        netString += (str(self.port) + MESSAGE_DELIMITER)
        netString += (self.role + MESSAGE_DELIMITER)
        netString += (str(self.alive))
        return netString

MESSAGE_HEAD = 'SERVERINFO' + MESSAGE_DELIMITER

def netStringToServer(netString):
    array = netString.split(MESSAGE_DELIMITER)
    ID = array[0]
    IP = array[1]
    port = int(array[2])
    role = array[3]
    alive = (array[4] == "True")
    return Server(ID, IP, port, role, alive)

def listToNetString(serverList):
    netString = MESSAGE_HEAD
    for s in serverList:
        netString += (s.toNetString() + MESSAGE_DELIMITER_BANG)
    netString = netString[:-1]
    return netString

def netStringToServerList(netString):
    netString = netString[len(MESSAGE_HEAD):]
    serverList = netString.split(MESSAGE_DELIMITER_BANG)
    return map(netStringToServer, serverList)
