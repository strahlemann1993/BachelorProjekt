import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(4, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(4,False) ## Turn on GPIO pin 7
