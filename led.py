# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO

ledPin = 17

# Zet de pinmode op Broadcom SOC.
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)


GPIO.setup(ledPin, GPIO.OUT)

print "Led aan"

GPIO.output(ledPin, GPIO.HIGH)
