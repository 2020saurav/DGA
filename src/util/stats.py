from config.networkParams import *

class Stats:
    '''
    This class is used to maintain counts of calls made and received, tasks processed
    '''
    def __init__(self, hostId):
        self.hashCheckQueryReceived = 0
        self.hashCheckQuerySent     = 0
        self.tasksProcessed         = 0
        self.tasksGranted           = 0
        self.hostId                 = hostId

    def toNetString(self):
        netString  = ''
        netString += (hostId + MESSAGE_DELIMITER)
        netString += (str(self.hashCheckQueryReceived) + MESSAGE_DELIMITER)
        netString += (str(self.hashCheckQuerySent) + MESSAGE_DELIMITER)
        netString += (str(self.tasksProcessed) + MESSAGE_DELIMITER)
        netString += str(self.tasksGranted)
        return netString

    def pprint(self):
        print "Host: ", self.hostId, "\tHCQR: ", self.hashCheckQueryReceived,
        print "\tHCQS: ", self.hashCheckQuerySent, "\tTasks processed: ", self.tasksProcessed,
        print "\tTasks Granted: ", self.tasksGranted

def statsNetStringToObject(netString):
    array = netString.split(MESSAGE_DELIMITER)
    hostId = array[0]
    stats = Stats(hostId)
    stats.hashCheckQueryReceived = int(array[1])
    stats.hashCheckQuerySent = int(array[2])
    stats.tasksProcessed = int(array[3])
    stats.tasksGranted = int(array[4])
    return stats
