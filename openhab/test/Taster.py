# Verwenden von GPIO
import RPi.GPIO as GPIO
import time
# Warnungen ausschalten
#GPIO.setwarnings(False)
# Pin Nummern verwenden
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
# Pin 11 als Input
GPIO.setup(22, GPIO.IN)
# Pin 12 als Output
GPIO.setup(4, GPIO.OUT)

# Endlosschleife
while True:
  # Solange Button nicht gedrueckt wird (False)
  if not GPIO.input(22):
    GPIO.output(4, True)
  # Wenn der Button gedrueckt wird
  else:
    GPIO.output(4, False)
#  time.sleep(1)
GPIO.cleanup() 
