import logging
import os
logDirectory = '../logs/'
def getLogger(name="None", logFile='dga.log'):
    logPath = logDirectory + logFile
    if not os.path.exists(os.path.dirname(logPath)):
        os.makedirs(os.path.dirname(logPath))
    formatter = logging.Formatter(
        '%(levelname)s: %(asctime)s %(funcName)s(%(lineno)d) -- %(message)s',
         datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(name)
    fh = logging.FileHandler(logPath)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    return logger
