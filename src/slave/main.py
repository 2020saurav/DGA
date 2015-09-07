import src.util.network as network
import src.util.server as server

class Main:
    ''' This Main class of Slave server is intended for following tasks:
    - Functions for acting on messages received by the listener
    - Receiving graph, config informations from master
    - Sending heartbeats
    - Processing tasks
    - Storing and sending result
    - ###
    '''
    def __init__(self):
        pass
    
    def saveServerInfo(self, netString):
        self.servers = server.netStringToServerList(netString) 

    def saveGraph(self, netString):
        pass

    def pushTaskToQueue(self, netString):
        pass

    def receivePoppedTask(self, netString):
        pass

    def startProcessing(self, netString):
        pass

    def grantTask(self, netString):
        # return netString of task
        pass

    def getPartialResult(self, netString):
        # return netString of result
        pass

    def checkHash(self, netString):
        # return netString of boolean response
        pass

    def processHashResponse(self, netString):
        pass

    def recordPing(self, netString):
        pass

    def recordPong(self, netString):
        pass

    def unrecognizedMessage(self, netString):
        pass

    def sendHeartBeatToMaster(self):
        pass
