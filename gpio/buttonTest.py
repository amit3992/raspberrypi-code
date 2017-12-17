import RPi.GPIO as GPIO

inPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(inPin,GPIO.IN)
print 'buttonTest running'

while True:
	value = GPIO.input(inPin)
	if value:
		print 'Not Pressed'
	else:
		print 'Pressed'

GPIO.cleanup()

