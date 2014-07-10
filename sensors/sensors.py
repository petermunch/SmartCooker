#! /usr/bin/python
__author__ = 'munchp'

import math
import sys

sys.path.append('.')
from max31855 import MAX31855

# In this example, I have the following setup:
#
# GND = P9.1
# VCC = P9.3
#
# data_pin = "GPIO1_15" # P8.15
# clk_pin = "GPIO1_14"  # P8.16
# cs_pin = "GPIO0_27"   # P8.17
#


def grill_temperature():
    grill_temp = MAX31855("GPIO1_15", "GPIO1_14", "GPIO0_27") #TODO: Change GPIO pins to something other
    return grill_temp.readCelsius()


def pit_temperature():
    pit_temp = MAX31855("GPIO1_15", "GPIO1_14", "GPIO0_27")
    return pit_temp.readCelsius()


#therm = MAX31855("GPIO1_15", "GPIO1_14", "GPIO0_27")
#tempintC = therm.readInternal()
#tempintF = therm.CtoF(tempintC)
#tempextC = therm.readCelsius()
#tempextF = therm.readFarenheit()

#if math.isnan(tempextC):
 #  print "Error reading Thermocouple - %s" % therm.readError()
#else:
  # print "Current internal temp = %.3f F, (%.3f C)" % (tempintF,tempintC)
   #print "Current thermocouple temp = %.3f F, (%.3f C)" % (tempextF,tempextC)
