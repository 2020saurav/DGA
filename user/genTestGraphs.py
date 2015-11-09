'''Module to generate test graphs'''
from random import randint
from random import sample
from subprocess import call
import sys

filename = "test"
def printUsage():
    print "Enter 1 n to generate star graph with n nodes"
    print "Enter 2 n to generate line graph with n nodes"
    print "Enter 3 n to generate a random tree with n nodes"
    print "Enter 4 n e to generate a graph with n nodes, and"
    print "each is added to the graph with probability e/nC2"

def star(n):
    sys.stdout = open(filename+'.txt','w')
    print n, n-1
    for i in range(1,n):
        print 0, i
    sys.stdout.close()

def line(n):
    sys.stdout = open(filename+'.txt','w')
    print n, n-1
    for i in range(0,n-1):
        print i, i+1
    sys.stdout.close()

def randTree(n):
    sys.stdout = open(filename+'.txt','w')
    print n, n-1
    for i in range(1, n):
        print i, randint(0,i-1)
    sys.stdout.close()

def randGraph(n, e):
    sys.stdout = open(filename+'.txt','w')
    edges = []
    nc2 = (n*(n-1))/2
    for i in range(0, n):
        for j in range(i+1, n):
            edges.append((i,j))
    graphEdges = sample(edges, e)
    print n, e
    for edge in graphEdges:
        print edge[0], edge[1]
    sys.stdout.close()

def doDotty():
    f = open(filename+".txt", 'r')
    sys.stdout = open(filename+'.dot','w')
    print "graph G"
    print "{"
    for line in f.readlines()[1:]:
        a,b = map(int, line.split(" "))
        print "node" + str(a) + " -- " + "node" + str(b)
    print "}"
    sys.stdout.close()
    f.close()
    call(["dot","-Tpng",filename+".dot","-o",filename+".png"])
    call(["gnome-open",filename+".png"])

if __name__ == '__main__':
    printUsage()
    try:
        inp = map(int, raw_input().split(" "))
        if inp[0] == 1:
            assert(inp[1] > 1)
            star(inp[1])
        elif inp[0] == 2:
            assert(inp[1] > 1)
            line(inp[1])
        elif inp[0] == 3:
            assert(inp[1] > 1)
            randTree(inp[1])
        elif inp[0] == 4:
            assert(inp[1] > 1)
            assert(inp[2] > 0 and inp[2] <= (inp[1]*(inp[1]-1)/2))
            randGraph(inp[1], inp[2])
        else:
            assert 0
        doDotty()
    except Exception, e:
        print e
        print "Wrong input format"
        printUsage()
