import RPi.GPIO as GPIO
import time

def my_callback(button):
	time.sleep(0.2)	#edge detector
	if GPIO.input(button) == False:
		GPIO.output(relay_pin, GPIO.HIGH)
		time.sleep(hold_time)
		GPIO.output(relay_pin, GPIO.LOW)



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

relay_pin = 4
button = 17
hold_time = 1

GPIO.setup(relay_pin, GPIO.OUT) # LED pin set as output

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

GPIO.add_event_detect(button, GPIO.FALLING, callback=my_callback)  # add rising edge detection on a channel

while(1):	
	time.sleep(1)
	
"""while(1):
	if GPIO.input(button) == False :
		time.sleep(0.3)
		if GPIO.input(button) == False:
			GPIO.output(relay_pin, GPIO.HIGH)
			time.sleep(hold_time)
			GPIO.output(relay_pin, GPIO.LOW)
		
"""
GPIO.cleanup() 
