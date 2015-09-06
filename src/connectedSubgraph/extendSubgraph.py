import copy
from config.networkParams import MESSAGE_DELIMITER
from src.graph.graph import Graph
from src.util.task import Task

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
                for outGoingEdge in self.graph.edgeList[a]:
                    if outGoingEdge != task.edges[i]:
                        newEdges.append(outGoingEdge)
                newVertices[a] = 1
            if task.vertices[b] == 0:
                for outGoingEdge in self.graph.edgeList[b]:
                    if outGoingEdge != task.edges[i]:
                        newEdges.append(outGoingEdge)
                newVertices[b] = 1
            newTasks.append(Task(newVertices, newEdges, newBloomHash, newServerHash))
        return newTasks

def preComputeTwoPow(p,maxEdges):
    twoPowModP = [1]
    for i in range(1,maxEdges):
        twoPowModP.append((twoPowModP[i-1]*2)%p)
    return twoPowModP
