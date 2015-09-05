import sys
sys.path.append('../config')
sys.path.append('../src/graph')
sys.path.append('../src/util')
sys.path.append('../src/connectedSubgraph')

from networkParams import MESSAGE_DELIMITER
from graph import Graph
from task import Task
from extendSubgraph import ExtendSubgraph
from initTasks import genInitalTasks

def testExtendSubgraph1():
    graph = Graph(5,5,[(0,1),(1,2),(2,3),(3,4),(4,0)])
    extender = ExtendSubgraph(graph, 101, 3)
    task = Task([0,1,1,0,0],[0,3],0,0)
    newTasks = extender.generateNewTasks(task)
    for task in newTasks:
        print task.vertices, task.edges

def testExtendSubgraph2():
    graph = Graph(3,2,[(0,1),(1,2)])
    extender = ExtendSubgraph(graph, 101, 3)
    task = Task([1,1,1], [], 0, 0)
    newTasks = extender.generateNewTasks(task)
    for task in newTasks:
        print task.vertices, task.edges

def testExtendSubgraph3():
    graph = Graph(3,3,[(0,1),(1,2),(0,2)])
    extender = ExtendSubgraph(graph, 101, 3)
    task = Task([1,1,1], [1], 0, 0)
    newTasks = extender.generateNewTasks(task)
    for task in newTasks:
        print task.vertices, task.edges

def testInitalTaskGeneration1():
    graph = Graph(5,5,[(0,1),(1,2),(2,3),(3,4),(4,0)])
    initalTasks = genInitalTasks(graph, 101, 5)
    for task in initalTasks:
        print task.vertices, task.edges

def testInitalTaskGeneration2():
    graph = Graph(3,3,[(0,1),(1,2),(0,2)])
    initalTasks = genInitalTasks(graph, 101, 5)
    for task in initalTasks:
        print task.vertices, task.edges

if __name__ == '__main__':
    testExtendSubgraph1()
    testExtendSubgraph2()
    testExtendSubgraph3()
    testInitalTaskGeneration1()
    testInitalTaskGeneration2()
