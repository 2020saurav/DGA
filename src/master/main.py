from config.servers import servers
from config.networkParams import *
from config.host import *
import src.util.network as network
import src.util.server as server
import src.util.logger as logger

log = logger.getLogger("Master-Main")

class Main:
    ''' This Main class of Master server is intended for following tasks:
    - Functions for acting on messages received by the listener
    - Passing graph, config informations to slaves
    - Collecting results
    - Receiving heartbeats
    - Allocating initial tasks to slaves
    '''
    def __init__(self):
        self.servers = servers

    def getServerListNetString(self):
        return server.listToNetString(servers)

    def processInput(self, netString):
        # Receive input from client. Parse it and form appropriate data structures
        pass

    def recordHeartBeat(self, netString):
        # Store heart beat information. Server ID will be present in message
        pass

    def recordPing(self, netString):
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
        log.debug("Unrecognized Message: " + netString)

    def sendPingForAliveTest(self, server):
        log.info('Sending ping to server ' + server.ID)
        netString = 'PING' + MESSAGE_DELIMITER + HOST_ID
        try:
            response = network.sendAndGetResponseFromIP(server.IP, server.port)
            log.info('PING response received from server ' + server.ID + ': '+ response)
            setServerAliveStatus(server.ID, True)
        except:
            response = None
            log.error('No PING response from server ' + server.ID + '. Marking it dead.')
            setServerAliveStatus(server.ID, False)

    def setServerAliveStatus(self, serverId, isAlive):
        for s in self.servers:
            if s.ID == serverId:
                s.alive = isAlive
                break

    def sendGraphToSlaves(self):
        aliveSlaves = filter(lambda s: s.role=='slave' and s.alive, self.servers)
        for slave in aliveSlaves:
            # form netString of Graph and do network.send
            pass

    def sendServerListToSlaves(self):
        aliveSlaves = filter(lambda s: s.role=="slave" and s.alive, servers)
        message = server.listToNetString(servers)
        for slave in aliveSlaves:
            network.sendToIP(slave.IP, slave.port, message)

    def sendInitialTaskToSlaves(self):
        pass

    def sendProcessStartNotification(self):
        aliveSlaves = filter(lambda s: s.role=="slave" and s.alive, servers)
        message = 'STARTPROCESSING'
        for slave in aliveSlaves:
            network.sendToIP(slave.IP, slave.port, message)       
