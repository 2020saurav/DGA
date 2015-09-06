import sys
sys.path.append('../')
from src.graph.graph import Graph
from src.graph.graph import stringToGraph

assert stringToGraph("3$011101110").toString()\
==  Graph(3,3,[(0,1),(1,2),(0,2)]).toString()
