import sys
sys.path.append('../config')
sys.path.append('../src/graph')
sys.path.append('../src/util')
sys.path.append('../src/connectedSubgraph')

from networkParams import MESSAGE_DELIMITER
from graph import Graph
from task import Task
import extendSubgraph

def testExtendSubgraph1():
    graph = Graph(5,5,[(0,1),(1,2),(2,3),(3,4),(4,0)])
    # extender = ExtendSubgraph(graph, 101, 3)
    task = Task([0,1,1,0,0],[2],0,0)
#     newTasks = extender.generateNewTasks(task)
#     print newTasks
    print graph,task

testExtendSubgraph1()
