import logging
import os
from config.logConfig import *

def getLogger(name="None", logFileName='dga.log'):
    logFilePath = os.path.join(LOG_DIRECTORY, logFileName)
    if not os.path.exists(os.path.dirname(logFilePath)):
        os.makedirs(os.path.dirname(logFilePath))
    formatter = logging.Formatter('[%(asctime)s] %(name)s [%(pathname)s:%(lineno)d] %(levelname)s - %(message)s')
    logger = logging.getLogger(name)
    fh = logging.FileHandler(logFilePath)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    return logger
