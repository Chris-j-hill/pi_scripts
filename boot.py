import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

relay_pin = 22
hold_time = 1

GPIO.setup(relay_pin, GPIO.OUT) # LED pin set as output

GPIO.output(relay_pin, GPIO.HIGH)
time.sleep(hold_time)
GPIO.output(relay_pin, GPIO.LOW)


GPIO.cleanup() 
