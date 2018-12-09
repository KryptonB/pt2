import logging, time

# default log level
logLevel = logging.DEBUG

# log file path and name
logFile = 'log/test.log'

# logging formats
#logFormat = '[ %(asctime)s ] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s'
#logFormat = '[%(asctime)s] %(levelname)s [Line: %(lineno)d] %(message)s'
logFormat = '[%(asctime)s] %(levelname)s (%(filename)s: %(lineno)d) %(message)s'


logging.basicConfig(filename=logFile, level=logLevel, format=logFormat)

def repea():
    while True :
        logging.warning('Hello Logging')
        time.sleep(1)

repea()
