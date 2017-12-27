#!/bin/python
 
ledPin = 7
 
# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
 
# Zet de pinmode op Broadcom SOC.
GPIO.setmode(GPIO.BCM)

# Zet waarschuwingen uit.
GPIO.setwarnings(False)
 
# Zet de GPIO pin als uitgang.
GPIO.setup(ledPin, GPIO.OUT)
 
# Zet de LED aan.
GPIO.output(ledPin, 1)