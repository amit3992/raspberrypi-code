import RPi.GPIO as GPIO
import time

pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

for i in range(0,20):
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(1)

GPIO.cleanup()
