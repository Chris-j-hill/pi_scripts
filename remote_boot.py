import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

relay_pin = 4
button = 17
hold_time = 1

GPIO.setup(relay_pin, GPIO.OUT) # LED pin set as output

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

while(1):
	if GPIO.input(button) == False :
		GPIO.output(relay_pin, GPIO.HIGH)
		time.sleep(hold_time)
		GPIO.output(relay_pin, GPIO.LOW)
	

GPIO.cleanup() 
