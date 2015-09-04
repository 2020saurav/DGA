import sys
sys.path.append('../src/graph')
sys.path.append('../config')
from graph import Graph, stringToGraph 

assert stringToGraph("3$011101110").toString()\
==  Graph(3,3,[(0,1),(1,2),(0,2)]).toString()
