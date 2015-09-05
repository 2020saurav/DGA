'''After setting up the system. 
i.e. stating the listener for master and all slaves
User runs this program to compute the result.
The input is passed to master which then handles 
everything aterwards.'''

import sys
sys.path.append('../src/graph')
sys.path.append('../src/util')
sys.path.append('../config')
from graph import Graph
from servers import servers
import socket
import network
import server
from networkParams import MESSAGE_DELIMITER
def readInput():
    '''First line contains two arguments
    n = number of vertices
    m = number of edges in the graph
    next m line conatins (a,b) reresenting an edge.'''
    n , m  = map(int,raw_input().split(" "))
    edges = []
    for i in range(0,m):
        a , b = map(int,raw_input().split(" "))
        edges.append((a,b))
    return n, m, edges

def findMasterIpPort():
    for s in servers :
        if s.role == 'master':
            return s.IP , s.port
    #master not found
    assert False

if __name__ == '__main__':
    n, m, edges = readInput()
    graph = Graph(n,m,edges).toString()
    MasterIP , MasterPort = findMasterIpPort()
    network.sendToIP(MasterIP,MasterPort,"INPUT"+MESSAGE_DELIMITER+graph)
    # TODO Wait for computation to end
    # merge all output file if required
