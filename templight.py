#!/usr/bin/env python
# Resources:
# https://www.instructables.com/Using-a-RPi-to-Control-an-RGB-LED/
import RPi.GPIO as GPIO
import time
import requests
import json

# Congifure GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RUNNING = True
green = 20
red = 21
blue = 16
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
Freq = 100
RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

# Turn the LED on
RED.start(1)
GREEN.start(1)
BLUE.start(1)

# Loop to get temp from API, then change LED color
try:
    while RUNNING:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=78757,us&appid={PUT KEY HERE}")
        temptemp = response.json()
        temperature = ((temptemp['main']['temp']) - 273.15)*1.8 + 32
        print(temperature)
        # Write function to accept temp, set vars for R, G, and B
        
        # Use R, G, and B set above in the following lines to set color
        # instead of using hardcoded values
        RED.ChangeDutyCycle(100)
        GREEN.ChangeDutyCycle(100)
        BLUE.ChangeDutyCycle(1)
        # Change sleep time after finishing code.  It is set low 
        # for testing purposes
        time.sleep(10)
except KeyboardInterrupt:
    RUNNING = False
    GPIO.cleanup()