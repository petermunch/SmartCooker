__author__ = 'munchp'

from twisted.internet import task
from twisted.internet import reactor
from sensors import sensors
from database import db_handler

timeout = 60.0  # Sixty seconds
pit_temp = sensors.pit_temperature()
grill_temp = sensors.grill_temperature()


def log_temp():
    print "Logging Pit Temperature as: %f" % pit_temp
    print "Logging Grill Temperature as: %f" % grill_temp
    db_handler.db_insert_pit(pit_temp)
    db_handler.db_insert_grill(grill_temp)
    pass


def run():
    l = task.LoopingCall(log_temp)
    l.start(timeout)  # call every sixty seconds
    reactor.run()
