import src.util.network as network
import src.util.server as server
import src.graph.graph as graph
import src.util.task as task
from src.util.bloom import BloomFilter
from src.connectedSubgraph.extendSubgraph import ExtendSubgraph
from config.networkParams import *
from random import randint
import time

TaskQueue = None
BloomHashFilter = None

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
        self.p = -1
        self.m = 0
        self.aliveSlaves = []
        self.servers = []
        self.initGraph = None
        self.graphProcessor = None
        pass

    '''Save the servers'''
    def saveServerInfo(self, netString):
        self.servers = server.netStringToServerList(netString)
        self.aliveSlaves = filter(lambda s : s.role=='slave' and s.alive, self.servers)
        self.m = len(aliveSlaves)

    '''Save the inital graph passed by master'''
    def saveGraph(self, netString):
        TaskQueue = Queue.Queue()
        BloomHashFilter = BloomFilter(10**7, 1e-7)
        self.initGraph = graph.stringToGraph(netString)

    def startProcessing(self, netString):
        taskRetries = 0
        self.graphProcessor = ExtendSubgraph(self.graph, self.p, self.m)
        while taskRetries < MAX_RETRIES :
            task = getNewTask(self)
            if task == None :
                taskRetries += 1
                continue
            else :
                taskRetries = 0
                newTasks = self.graphProcessor.generateNewTasks(task)
                for newTask in newTasks :
                    if checkUniquenessOfTask(newTask.bloomHash, self.aliveSlaves[serverHash]) :
                       TaskQueue.put(newTask)

    def getPartialResult(self, netString):
        # return netString of result
        pass

    def recordPing(self, netString):
        pass

    def unrecognizedMessage(self, netString):
        pass

    def sendHeartBeatToMaster(self):
        pass

def grantTask():
    # return netString of task
    # return 'EMPTYTASK' if task queue is empty currently
    # else return a task prepended with 'POPPEDTASK'
    if TaskQueue.empty() :
        return EMPTYTASK
    else :
        poppedTask = TaskQueue.get()
        message = POPPEDTASK + MESSAGE_DELIMITER + poppedTask.toNetString()
        return message

'''Insert a given task in the task queue'''
def pushTaskToQueue(netString):
    TaskQueue.put(task.toTaskFromNetString(netString))

''' Put a given hash into bloom filter '''
def putHash(message):
    # @Depricated
    pass

'''Check a given hash, insert the hash if it was not present already
    and return the response'''
def checkHash(message):
    hashToCheck = int(message)
    return HASHRESPONSE + MESSAGE_DELIMITER +\
            BloomHashFilter.checkAndInsert(hashToCheck)

'''Given a task return true if it has not been seen yet'''
def checkUniquenessOfTask(bloomHash, slaveToContact):
    # TODO optimize to aviod network call if server is local
    message = HASHCHECK + MESSAGE_DELIMITER + str(bloomHash)
    hashCheckResponse = network.sendAndGetResponseFromIP(
            slaveToContact.IP,
            slaveToContact.port,
            message)
    # Note : this call will simultaneously put the hash
    # into the bloom filter if it was not present already
    words = hashCheckResponse.split(MESSAGE_DELIMITER)
    return not bool(words[1])

'''Get a new task,
first check the local task queue for a task
if no task is found then try to get task from a random slave
if that also fails then wait and return None'''
def getNewTask(main):
    if not TaskQueue.empty() :
        return TaskQueue.get()
    else :
        randomSlave = main.aliveSlaves[randint(0,main.m)]
        newTaskString = network.sendAndGetResponseFromIP(
            randomSlave.IP,
            randomSlave.port,
            REQUESTTASK)
        words = newTaskString.split(MESSAGE_DELIMITER)
        messageHead = words[0]
        if messageHead == EMPTYTASK :
            time.sleep(UNSUCCESSFUL_GET_TASK_WAIT_TIME)
            return None
        else :
            return task.toTaskFromNetString(MESSAGE_DELIMITER.join(words[1:]))
