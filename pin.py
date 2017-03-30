#!/usr/bin/python3
import sys, RPi.GPIO as GPIO
#pin = 7
pin = sys.argv[1]
pin = int(pin)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

if (GPIO.input(pin) == 1):
        GPIO.output(pin, 0)
else:
        GPIO.output(pin, 1)
