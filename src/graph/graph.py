import sys
import thread
sys.path.append('../../config')
from networkParams import MESSAGE_DELIMITER

class Graph(object):
    """docstring for Graph
    A class to store graph information for 
    small graphs.
    n is number of vertices
    m is number of edges
    edges is list of (a,b) , where a and b are vertices
    """
    def __init__(self, n, m, edges):
        assert len(edges) == m
        self.n = n
        self.m = m
        self.adjMat = []
        for i in range(0,n):
            self.adjMat.append([0]*n)
        self.adjList = []
        for i in range(0,n):
            self.adjList.append([])
        for edge in edges:
            self.adjMat[edge[0]][edge[1]]=1
            self.adjMat[edge[1]][edge[0]]=1
        self.edges = []
        """All the edges will be numbered in this way."""
        for i in range(0,n):
            for j in range(i+1,n):
                if self.adjMat[i][j] == 1 :
                    self.edges.append((i,j))

    def toString(self):
        graph = str(self.n)+MESSAGE_DELIMITER
        for i in range(0,self.n):
            for j in range(0,self.n):
                graph += str(self.adjMat[i][j])
        return graph

def stringToGraph(graph):
        n , edgesBitArray = graph.split(MESSAGE_DELIMITER)
        n = int(n)
        edges = []
        for i in range(0,n):
            for j in range(i+1,n):
                if edgesBitArray[i*n + j] == '1':
                    edges.append((i,j))
        newGraph = Graph(n, len(edges), edges)
        return newGraph
