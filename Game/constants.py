#!/usr/bin/python

# description: pin definitions, LCD comments
# Author: Tony Tran and Brandon Vu

import RPi.GPIO as GPIO

# LED pin definitions
led_1 = 2
led_2 = 12
led_3 = 21
led_4 = 10

# button pin definitions
btn_1 = 18 
btn_2 = 17
btn_3 = 22
btn_4 = 27

#suppress warnings
GPIO.setwarnings(False)

# set mode
GPIO.setmode(GPIO.BCM)

# LED setup
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(led_4, GPIO.OUT)

# button setup to pull up and input
GPIO.setup(btn_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
