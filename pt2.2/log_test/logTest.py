import logging, time

#logFormat = '[ %(asctime)s ] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s'
logFormat = '[%(asctime)s] %(levelname)s (%(filename)s: %(lineno)d) %(message)s'
#logFormat = '[%(asctime)s] %(levelname)s [Line: %(lineno)d] %(message)s'
logging.basicConfig(filename='hehe.log', level=logging.DEBUG, format=logFormat)

def repea():
    while True :
        logging.warning('Hello Logging')
        time.sleep(1)

repea()
