from config.servers import servers
from config.networkParams import *
import src.util.network as network
import src.util.server as server

class Main:
    ''' This Main class of Master server is intended for following tasks:
    - Functions for acting on messages received by the listener
    - Passing graph, config informations to slaves
    - Collecting results
    - Receiving heartbeats
    - Allocating initial tasks to slaves
    '''
    def __init__(self):
        # TODO
        pass

    def getServerListNetString(self):
        return server.listToNetString(servers)

    def sendServerListToSlaves(self):
        # We are sending details of Master server also to alive slaves
        # Slaves should figure out alive slaves and Master server themselves from this information
        slaves = filter(lambda s: s.role=="slave" and s.alive, servers)
        message = server.listToNetString(servers)
        for slave in slaves:
            network.sendToIP(slave.IP, slave.port, message)

    def processInput(self, netString):
        # Receive input from client. Parse it and form appropriate data structures
        pass

    def recordHeartBeat(self, netString):
        # Store heart beat information. Server ID will be present in message
        pass

    def recordPing(self, netString):
        # Log this
        pass

    def recordPong(self, netString):
        # Log this
        pass

    def processPartialResult(self, netString):
        # parse result from a slave and store it to finally merge all results
        pass

    def recordJobCompleteNotification(self, netString):
        # Increase count of slaves with completed tasks
        # Ask for partial result(?) or ask when all slaves are done
        pass

    def unrecognizedMessage(self, netString):
        # Log this
        pass
