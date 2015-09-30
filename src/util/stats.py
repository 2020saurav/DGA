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
        self.timeTaken              = 0
        self.hostId                 = hostId

    def reset(self):
        self.hashCheckQueryReceived = 0
        self.hashCheckQuerySent     = 0
        self.tasksProcessed         = 0
        self.tasksGranted           = 0
        self.timeTaken              = 0

    def toNetString(self):
        netString  = ''
        netString += (self.hostId + MESSAGE_DELIMITER)
        netString += (str(self.hashCheckQueryReceived) + MESSAGE_DELIMITER)
        netString += (str(self.hashCheckQuerySent) + MESSAGE_DELIMITER)
        netString += (str(self.tasksProcessed) + MESSAGE_DELIMITER)
        netString += (str(self.tasksGranted) + MESSAGE_DELIMITER )
        netString += (str(self.timeTaken))
        return netString

    def pprint(self):
        print "Host: ", self.hostId, "\tHCQR: ", self.hashCheckQueryReceived,
        print "\tHCQS: ", self.hashCheckQuerySent, "\tTasks Processed: ", self.tasksProcessed,
        print "\tTasks Granted: ", self.tasksGranted, "\tTime Taken: ", self.timeTaken

def statsNetStringToObject(netString):
    array = netString.split(MESSAGE_DELIMITER)
    hostId = array[0]
    stats = Stats(hostId)
    stats.hashCheckQueryReceived = int(array[1])
    stats.hashCheckQuerySent = int(array[2])
    stats.tasksProcessed = int(array[3])
    stats.tasksGranted = int(array[4])
    stats.timeTaken = float(array[5])
    return stats
