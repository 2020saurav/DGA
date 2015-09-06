'''Module to handle all i/o's for master.'''
import sys
sys.path.append('../../')

from src.graph.graph import Graph
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
    graph = Graph(n,m,edges)
    print graph.toString()
