# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
import time

greenPin = 17
redPin = 27

# Zet de pinmode op Broadcom SOC.
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)


GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)


while True:
	
	print "Groen aan / rood uit"
	GPIO.output(greenPin, GPIO.HIGH)
	GPIO.output(redPin, GPIO.LOW)
	time.sleep(1)

	print "Groen aan / rood uit"
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(redPin, GPIO.HIGH)
	time.sleep(1)
