import sys
import copy
sys.path.append('../../config')
sys.path.append('../graph')
sys.path.append('../util')
from networkParams import MESSAGE_DELIMITER
from graph import Graph
from task import Task

'''Function to create inital tasks given graph as input'''

def genInitalTasks(graph, p, m):
    tasks = []
    edgeNumber = 0
    for edge in graph.edges:
        taskVertices = [0]*graph.n
        taskVertices[edge[0]] = taskVertices[edge[1]] = 1
        taskEdges = []
        for outgoingEdge in graph.edgeList[edge[0]]:
            if outgoingEdge != edgeNumber :
                taskEdges.append(outgoingEdge)
        for outgoingEdge in graph.edgeList[edge[1]]:
            if outgoingEdge != edgeNumber :
                taskEdges.append(outgoingEdge)
        edgeNumber += 1
        taskBloomHash = (2**edgeNumber)%p
        taskServerHash = (2**edgeNumber)%m
        tasks.append(Task(taskVertices, taskEdges, taskBloomHash, taskServerHash))
    return tasks
    