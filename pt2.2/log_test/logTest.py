import logging
import time
import datetime

# default log level
logLevel = logging.DEBUG

# log file path and name
logFile = 'log/test.log'

# if you want to add the datetimestamp to the log file, do this
# and use logFileWithDatestamp as the log file name
now = datetime.datetime.now()
fileDatestamp = now.strftime('%Y-%m-%d_%H%M%S')
logFileWithDatestamp = 'log/test_' + fileDatestamp + '.log'


# differnt logging formats. Choose the one you like
#logFormat = '[ %(asctime)s ] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s'
#logFormat = '[%(asctime)s] %(levelname)s [Line: %(lineno)d] %(message)s'
logFormat = '[%(asctime)s] %(levelname)s (%(filename)s: %(lineno)d) %(message)s'


logging.basicConfig(filename=logFile, level=logLevel, format=logFormat)

def repea():
    while True :
        logging.warning('Hello Logging')
        time.sleep(1)

repea()
