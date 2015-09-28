from config.networkParams import MESSAGE_DELIMITER
from src.graph.graph import Graph
from src.util.task import Task

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
        taskBloomHash = (2**edgeNumber)%p
        taskServerHash = (2**edgeNumber)%m
        tasks.append(Task(taskVertices, taskEdges, taskBloomHash, taskServerHash))
        edgeNumber += 1
    return tasks
