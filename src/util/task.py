from config.networkParams import *

class Task:
    ''' Task contains necessary information to process the subgraph.
    Since we intend to proceed by growing edges, we need to keep the list edges we can grow in the 
    next step, list of vertices already processed, bloom-filter hash and the slave hash.
    '''
    '''
    vertices : list of vertex which are already in the subgraph
    edges : serial number of edges which can be grown in the next step
    bloomHash : ###
    serverHash : ###
    '''
    def __init__(self, vertices, edges, bloomHash, serverHash): 
        self.vertices = vertices
        self.edges = edges
        self.bloomHash = bloomHash
        self.serverHash = serverHash

    ''' Convert the object to a string to transfer over the network
    '''
    def toNetString(self):
        netString = ''
        edgeCount = len(self.edges)
        verticesString = "".join(map(str, self.vertices))
        edgesString = MESSAGE_DELIMITER.join(map(str, self.edges))
        netString += (verticesString + MESSAGE_DELIMITER)
        netString += (str(edgeCount) + MESSAGE_DELIMITER)
        netString += (edgesString + MESSAGE_DELIMITER)
        netString += (str(self.bloomHash) + MESSAGE_DELIMITER)
        netString += (str(self.serverHash))
        return netString

''' Convert a netString to a Task object.
(not in Task Class)
'''
def toTaskFromNetString(netString):
    array = netString.split(MESSAGE_DELIMITER)
    vertices = map(lambda c: int(c), array[0])
    edgeCount = int(array[1])
    edges = map(lambda i: int(i), array[2:-2])
    bloomHash = array[-2]
    serverHash = array[-1]
    return Task(vertices, edges, bloomHash, serverHash)
