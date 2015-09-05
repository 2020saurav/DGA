import sys
sys.path.append('../src/util')
sys.path.append('../config')

from task import Task
import task

def testNetStringConversion():    
    vertices = [1, 0, 1 , 1] # which vertices are present in subgraph
    edges = [1, 3 , 4] # index of edges present in subgraph
    bloomHash = 'hash1'
    serverHash = 'hash2'
    expectedString = "1011$3$1$3$4$hash1$hash2"
    t = Task(vertices, edges, bloomHash, serverHash)
    assert t.toNetString() == expectedString
    print "To Net String Conversion Passed"

def testObjectConversion():
    netString = "1011$3$1$3$4$hash1$hash2"
    t = task.toTaskFromNetString(netString)
    assert t.vertices == [1, 0, 1, 1]
    assert t.edges == [1, 3, 4]
    assert t.bloomHash == 'hash1'
    assert t.serverHash == 'hash2'
    assert t.toNetString() == netString
    print "To Object Conversion Passed"

def testPushPoppedTaskConversion():
    netString = "1011$3$1$3$4$hash1$hash2"
    t = task.toTaskFromNetString(netString)
    t1 = task.toTaskFromPoppedTaskString(t.getPoppedTaskString())    
    assert t1.toNetString() == netString
    
    t2 = task.toTaskFromPushTaskString(t1.getPushTaskString())    
    assert t2.toNetString() == netString

    print "Push Popped Task Conversion Passed"
if __name__ == '__main__':
    testNetStringConversion()
    testObjectConversion()
    testPushPoppedTaskConversion()
