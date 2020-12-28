import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=1)

GPIO.output(17, 0)
time.sleep(2)
GPIO.output(17, 1)
