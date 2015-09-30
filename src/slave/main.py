import src.util.network as network
import src.util.server as server
import src.graph.graph as graph
import src.util.task as task
from src.util.bloom import BloomFilter
from src.util.stats import Stats
from src.connectedSubgraph.extendSubgraph import ExtendSubgraph
from config.networkParams import *
from config.host import *
from config.messageHeads import *
from random import randint
import src.util.logger as logger
import time
import Queue

# TODO save a graph to a persistent file before pushing it into the task queue
TaskQueue = Queue.Queue()
BloomHashFilter = BloomFilter(10**7, 1e-7)

log = logger.getLogger("Slave-Main")
stats = Stats(HOST_ID)

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
        self.p = None
        self.m = None
        self.aliveSlaves = []
        self.servers = []
        self.initGraph = None
        self.graphProcessor = None
        # Currently lock is not required as this will be used
        self.taskCounter = None

    '''Save the servers'''
    def saveServerInfo(self, netString):
        self.servers = server.netStringToServerList(netString)
        self.aliveSlaves = filter(lambda s : s.role=='slave' and s.alive, self.servers)
        self.m = len(self.aliveSlaves)
        log.info("Server informations saved")

    '''Save the inital graph passed by master'''
    def saveGraph(self, netString):
        self.initGraph = graph.stringToGraph(netString)
        log.info("Graph saved")

    def startProcessing(self, netString):
        taskRetries = 0
        stats.reset()
        self.startTime = time.time()
        log.info('Processing started')
        while True:
            if (self.p != None and self.m != None and self.initGraph != None):
                break
            log.debug("Waiting for initialization.")
            time.sleep(WAIT_FOR_INITIALIZATION)
        self.graphProcessor = ExtendSubgraph(self.initGraph, self.p, self.m)
        while taskRetries < MAX_RETRIES :
            task = getNewTask(self)
            # TODO remove this later
            if task == None :
                taskRetries += 1
                log.debug("No new task found")
                continue
            else :
                log.debug("Task's string : " + task.toNetString())
                stats.tasksProcessed += 1
                taskRetries = 0
                newTasks = self.graphProcessor.generateNewTasks(task)
                for newTask in newTasks :
                    if checkUniquenessOfTask(newTask.bloomHash, self.aliveSlaves[newTask.serverHash]) :
                       TaskQueue.put(newTask)
        log.info('Task complete')
        self.sendJobCompletionNotiToMaster()
        # TODO send job completion notification to master

    def getPartialResult(self, netString):
        # return netString of result
        pass

    def recordPing(self, netString):
        log.info("Responded to master's ping.")

    def unrecognizedMessage(self, netString):
        log.error("Unrecognized Message received " + netString)

    def sendHeartBeatToMaster(self):
        pass

    def saveNetworkPrime(self,message):
        self.p = int(message)
        log.info("Prime saved")

    def sendJobCompletionNotiToMaster(self):
        masterServer = filter(lambda s : s.role=='master' and s.alive, self.servers)[0]
        endTime = time.time()
        stats.timeTaken = endTime - self.startTime
        network.sendToIP(masterServer.IP, masterServer.port,
            JOBCOMPLETE + MESSAGE_DELIMITER + stats.toNetString())
        log.info("Job completion notification sent")
        # Clean bloom filter and wait for next input
        BloomHashFilter.clean()


def grantTask():
    # return netString of task
    # return 'EMPTYTASK' if task queue is empty currently
    # else return a task prepended with 'POPPEDTASK'
    if TaskQueue.empty() :
        log.debug("Empty Task returned")
        return EMPTYTASK
    else :
        poppedTask = TaskQueue.get()
        message = POPPEDTASK + MESSAGE_DELIMITER + poppedTask.toNetString()
        stats.tasksGranted += 1
        log.debug("Popped Task returned")
        return message

'''Insert a given task in the task queue'''
def pushTaskToQueue(netString):
    TaskQueue.put(task.toTaskFromNetString(netString))
    log.info("Task pushed in queue")

''' Put a given hash into bloom filter '''
def putHash(message):
    # @Depricated
    pass

'''Check a given hash, insert the hash if it was not present already
    and return the response'''
def checkHash(message):
    hashToCheck = int(message)
    # log.info('Hash check query received')
    stats.hashCheckQueryReceived += 1
    return HASHRESPONSE + MESSAGE_DELIMITER + str(BloomHashFilter.checkAndInsert(hashToCheck))

'''Given a task return true if it has not been seen yet'''
def checkUniquenessOfTask(bloomHash, slaveToContact):
    # TODO optimize to aviod network call if server is local
    message = HASHCHECK + MESSAGE_DELIMITER + str(bloomHash)
    # if slaveToContact is itself
    if slaveToContact.ID == HOST_ID:
        return not BloomHashFilter.checkAndInsert(bloomHash)

    hashCheckResponse = network.sendAndGetResponseFromIP(
            slaveToContact.IP,
            slaveToContact.port,
            message)
    stats.hashCheckQuerySent += 1
    # Note : this call will simultaneously put the hash
    # into the bloom filter if it was not present already
    words = hashCheckResponse.split(MESSAGE_DELIMITER)
    return not (words[1]=='True')

'''Get a new task,
first check the local task queue for a task
if no task is found then try to get task from a random slave
if that also fails then wait and return None'''
def getNewTask(main):
    if not TaskQueue.empty() :
        return TaskQueue.get()
    else :
        randomSlave = main.aliveSlaves[randint(0, main.m - 1)]
        newTaskString = network.sendAndGetResponseFromIP(
            randomSlave.IP,
            randomSlave.port,
            REQUESTTASK)
        words = newTaskString.split(MESSAGE_DELIMITER)
        messageHead = words[0]
        if messageHead == EMPTYTASK :
            time.sleep(UNSUCCESSFUL_GET_TASK_WAIT_TIME)
            return None
        elif messageHead == POPPEDTASK :
            return task.toTaskFromNetString(MESSAGE_DELIMITER.join(words[1:]))
        else :
            main.unrecognizedMessage()
