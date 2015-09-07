from config.servers import servers
from config.networkParams import *
from config.host import *
from config.messageHeads import *
import src.util.network as network
import src.util.server as server
import src.util.logger as logger
import src.connectedSubgraph.initTasks as initTasks
import src.util.primes as primes
import src.graph.graph as graph
from random import randint

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
        self.servers = getServersAfterPingTests(servers)
        self.graph = None
        self.aliveSlaves = filter(lambda s: s.role=='slave' and s.alive, self.servers)
        self.m = len(self.aliveSlaves)
        self.p = primes.getLargeRandomPrime()

    def getServerListNetString(self):
        return server.listToNetString(servers)

    def processInput(self, netString):
        self.graph = graph.stringToGraph(netString)

    def recordHeartBeat(self, netString):
        # Store heart beat information. Server ID will be present in message
        pass

    def recordPing(self, netString):
        log.info('PING received from server ID ' + netString)

    def processPartialResult(self, netString):
        # parse result from a slave and store it to finally merge all results
        pass

    def recordJobCompleteNotification(self, netString):
        # Increase count of slaves with completed tasks
        # Ask for partial result(?) or ask when all slaves are done
        pass

    def unrecognizedMessage(self, netString):
        log.debug("Unrecognized Message: " + netString)

    def sendGraphToSlaves(self):
        message = GRAPH + MESSAGE_DELIMITER + self.graph.toString()
        for slave in self.aliveSlaves:
            network.sendToIP(slave.IP, slave.port, message)
            log.info("Graph sent to server " + slave.ID)

    def sendServerListToSlaves(self):
        message = SERVERINFO + MESSAGE_DELIMITER
        message += server.listToNetString(self.servers)
        for slave in self.aliveSlaves:
            network.sendToIP(slave.IP, slave.port, message)
            log.info("Server list sent to server " + slave.ID)

    def sendInitialTaskToSlaves(self):
        tasks = initTasks.genInitalTasks(self.graph, self.p, self.m)
        for t in tasks:
            slaveIndex = randint(0, len(aliveSlaves))
            slaveServer = aliveSlaves[slaveIndex]
            message = PUSHTASK + MESSAGE_DELIMITER
            message += t.toNetString()
            network.sendToIP(slaveServer.IP, slaveServer.port, message)
            log.info("Initial task sent to server " + slaveServer.ID)

    def sendProcessStartNotification(self):
        message = STARTPROCESSING
        for slave in self.aliveSlaves:
            network.sendToIP(slave.IP, slave.port, message)
            log.info("Start Processing message sent to server " + slave.ID)      

def getServersAfterPingTests(servers):
    for s in servers:
        s.alive = network.sendPingForAliveTest(s)
        log.info("Server " + s.ID + " alive: " + str(s.alive))
    return servers
