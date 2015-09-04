import sys
sys.path.append('../../config')
sys.path.append('../util')

import network
import server

class Main:
    ''' This Main class of Slave server is intended for following tasks:
    - Functions for acting on messages received by the listener
    - Receiving graph, config informations from master
    - Sending heartbeats
    - Processing tasks
    - Storing and sending result
    - ###
    '''
    def __init__(self):
        pass
    
    def saveServerInfo(self, netString):
        self.servers = server.netStringToServerList(netString) 
        print self.servers
