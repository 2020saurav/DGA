import src.util.network as network
import src.util.server as server
import src.graph.graph as graph
import src.util.task as task
from src.util.bloom import BloomFilter
from src.connectedSubgraph import ExtendSubgraph
from config.networkParams import *

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
            # TODO getNewTask return a task else none
            task = getNewTask(TaskQueue)
            if task == None :
                taskRetries += 1
                continue
            else :
                taskRetries = 0
                newTasks = self.graphProcessor.generateNewTasks(task)
                for tasks in newTasks :
                    # TODO checkUniquenessOfTask
                    if checkUniquenessOfTask(tasks) :
                       TaskQueue.put(tasks)

    def grantTask(self, netString):
        # return netString of task
        pass

    def getPartialResult(self, netString):
        # return netString of result
        pass

    def recordPing(self, netString):
        pass

    def unrecognizedMessage(self, netString):
        pass

    def sendHeartBeatToMaster(self):
        pass

'''Insert a new task in the task queue'''
def pushTaskToQueue(netString):
    TaskQueue.put(task.toTaskFromNetString(netString))

''' Put a given hash into bloom filter '''
def putHash(message):
    pass

'''Check a given hash and return the response'''
def checkHash(message):
    pass

'''Return the task represented by given string.'''
def receivePoppedTask(self, netString):
    return task.toTaskFromNetString(netString)

'''Given a task return true if it has not been seen yet'''
def checkUniquenessOfTask():
    pass

'''Get a new task,
first check the local task queue for a task
if no task is found then try to get task from a random slave
if that also fails then wait and return None'''
def getNewTask():
    pass