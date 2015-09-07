import src.util.network as network
import src.util.server as server
import src.graph.graph as graph
import src.util.task as task
from config.networkParams import *
import Queue

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
        # TODO set these value
        # p
        pass

    '''Save the selfrvers'''
    def saveServerInfo(self, netString):
        self.servers = server.netStringToServerList(netString)
        self.aliveSlaves = filter(lambda s : s.role=='slave' and s.alive, self.servers)
        self.m = len(aliveSlaves)

    '''Save the inital graph passed by master'''
    def saveGraph(self, netString):
        self.initGraph = graph.stringToGraph(netString)

    '''Return the task represented by given string.'''
    def receivePoppedTask(self, netString):
        return task.toTaskFromNetString(netString)

    def startProcessing(self, netString, taskQueue):
        taskRetries = 0
        graphProcessor = ExtendSubgraph(self.graph, self.p, self.m)
        while taskRetries < MAX_RETRIES :
            # TODO getNewTask return a task else none
            task = getNewTask(taskQueue)
            if task == None :
                taskRetries += 1
                continue
            else :
                taskRetries = 0
                newTasks = graphProcessor.generateNewTasks(task)
                for tasks in newTasks :
                    # TODO checkUniquenessOfTask
                    if checkUniquenessOfTask(tasks) :
                       taskQueue.put(tasks)

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

    def unrecognizedMessage(self, netString):
        pass

    def sendHeartBeatToMaster(self):
        pass

'''Insert a new task in the task queue'''
def pushTaskToQueue(netString, taskQueue):
    taskQueue.put(task.toTaskFromNetString(netString))
