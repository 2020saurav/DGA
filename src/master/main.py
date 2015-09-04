import sys
sys.path.append('../../config')
sys.path.append('../util')

from servers import servers
import network
import server

class Main:
    ''' This Main class of Master server is intended for following tasks:
    - Functions for acting on messages received by the listener
    - Passing graph, config informations to slaves
    - Collecting results
    - Receiving heartbeats
    - Allocating initial tasks to slaves
    '''
    def __init__(self):
        pass

    def getServerListNetString(self):
        return server.listToNetString(servers)
