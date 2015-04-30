#!/usr/bin/python

# Import required Python libraries
#import RPi.GPIO as GPIO
import time
import ISY
import sys

#print sys.argv[1]

myisy = ISY.Isy(addr="192.168.0.55", userp="admin", userl="admin")
lamp_light = myisy.get_node("Room Lamp")
lamp_light.on(sys.argv[1])

# Use BCM GPIO references instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)

# init list with pin numbers

#pinList = [15]

# loop through pins and set mode and state to 'low'

# for i in pinList:
#     GPIO.setwarnings(False)
#     GPIO.setup(i, GPIO.OUT)
#     GPIO.output(i, GPIO.HIGH)
#
# def trigger() :
#         for i in pinList:
#           GPIO.output(i, GPIO.HIGH)
# #         GPIO.cleanup()
#           break
#
#
# try:
#     trigger()
#
#
# except KeyboardInterrupt:
#   print "  Quit"
#   # Reset GPIO settings
#   GPIO.cleanup()
