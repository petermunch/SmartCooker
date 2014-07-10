__author__ = 'munchp'

import time
import logging
import threading
from webserver import main as web_main
from timemachine import temp_logger, time_handler


logging.basicConfig(level=logging.DEBUG)  # format='[(%levelname)s] (%threadName)-10s) %(message)s',)


def web_worker():
    logging.debug('Starting Server Thread')
    web_main.main()
    time.sleep(3)
    logging.debug('Exiting Server Thread')


def temperature_service():
    logging.debug('Starting')
    temp_logger.run()
    time.sleep(5)
    logging.debug('Exiting')

tempThread = threading.Thread(name='temperature_service', target=temperature_service)
serverThread = threading.Thread(name='web_worker', target=web_worker)


def main():
    #threading.Thread(target=webserver_main.server()).start()
    #webserver_main.server()
    #threading.Thread(target=temp_logger.reactor.run()).start()
    #temp_logger.reactor.run()
    #seconds = datetime.time.second()
    #print seconds
    print "Starting SmartCooker Now"

    tempThread.start()
    serverThread.start()

if __name__ == "__main__":
    main()