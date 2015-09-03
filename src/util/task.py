import sys
sys.path.append('../../config')

from networkParams import *

class Task:
    ''' Task contains necessary information to process the subgraph.
    Since we intend to proceed by growing edges, we need to keep the list edges we can grow in the 
    next step, list of vertices already processed, bloom-filter hash and the slave hash.
    '''
    '''
    vertices : list of vertex which are already in the subgraph
    edges : serial number of edges which can be grown in the next step
    bloomHash : ###
    slaveHash : ###
    '''
    def __init__(self, vertices, edges, bloomHash, slaveHash): 
        self.vertices = vertices
        self.edges = edges
        self.bloomHash = bloomHash
        self.slaveHash = slaveHash

    ''' Convert the object to a string to transfer over the network
    '''
    def toNetString(self):
        netString = ''
        # Pattern: <Num of total vertices> Delim <Zero One string of vertices present> Delim
        # <Num of edges> Delim <e1> Delim ... Delim <en> Delim <bloomHash> Delim <slaveHash>
        return netString


''' Convert a netString to a Task object.
(not in Task Class)
'''
def toTaskObject(netString):
    pass

