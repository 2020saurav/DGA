import copy
from config.networkParams import MESSAGE_DELIMITER
from config.networkParams import DUMMY_PROC_WAIT_TIME
from src.graph.graph import Graph
from src.util.task import Task
import time

''' Module to extend the subgraph.
    Constructer is initialized by graph structure (n, m, adjacency list
    and adjacency matrix) and prime used for hashing the subgraphs and
    number of slaves.
'''
class ExtendSubgraph:
    def __init__(self, graph, p, m, maxEdges = 100):
        self.graph = graph
        self.p = p
        self.m = m
        self.twoPowModP = preComputeTwoPow(p,maxEdges)
        self.twoPowModM = preComputeTwoPow(m,maxEdges)

    '''Given a  and a task (vertices, edges, bloomhash
    server hash), generate new task by extending the subgraph.'''
    def generateNewTasks(self,task):
        self.computeAndSave(task)
        numTasks = len(task.edges)
        newTasks = []
        for i in range(0,numTasks):
            newVertices = copy.deepcopy(task.vertices)
            newEdges = []
            for j in range(0, numTasks):
                if i != j:
                    newEdges.append(task.edges[j])
            newBloomHash = (task.bloomHash + self.twoPowModP[task.edges[i]])%self.p
            newServerHash = (task.serverHash + self.twoPowModM[task.edges[i]])%self.m
            a , b = self.graph.edges[task.edges[i]]
            if task.vertices[a] == 0:
                newVertices[a] = 1
                for outGoingEdge in self.graph.edgeList[a]:
                    u , v = self.graph.edges[outGoingEdge]
                    if newVertices[u]==0 or newVertices[v]==0:
                        newEdges.append(outGoingEdge)
            if task.vertices[b] == 0:
                newVertices[b] = 1
                for outGoingEdge in self.graph.edgeList[b]:
                    u , v = self.graph.edges[outGoingEdge]
                    if newVertices[u]==0 or newVertices[v]==0:
                        newEdges.append(outGoingEdge)
            newTasks.append(Task(newVertices, newEdges, newBloomHash, newServerHash))
        return newTasks

    '''Subroutine / proc to be performed on each computed subgraph goes here
        currently it's a dummy function which waits for few milliseconds'''
    def computeAndSave(self,task):
        '''task contains sufficient information to do any kind of computation of subraph'''
        time.sleep(DUMMY_PROC_WAIT_TIME)
        return

def preComputeTwoPow(p,maxEdges):
    twoPowModP = [1]
    for i in range(1,maxEdges):
        twoPowModP.append((twoPowModP[i-1]*2)%p)
    return twoPowModP
