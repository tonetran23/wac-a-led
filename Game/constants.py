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

# LCD pin definitions
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11

# Buzzer pin definitions
buz = 20

# LCD constants definitions
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
E_PULSE = 0.0005  # Timing constants
E_DELAY = 0.0005

#suppress warnings
GPIO.setwarnings(False)

# set mode
GPIO.setmode(GPIO.BCM)

# LED setup
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(led_4, GPIO.OUT)

# GPIO setup for pins
GPIO.setup(btn_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_D4, GPIO.OUT)
GPIO.setup(LCD_D5, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D6, GPIO.OUT)
GPIO.setup(LCD_D7, GPIO.OUT)
GPIO.setup(buz, GPIO.OUT)

# Defining lists
neg_comments = ["You SUCK!", "HAHA! LOSER!", "Good job! SIKE!", "Slowpoke!!", "You sad?? :(", "Not even close", "LLLLLLL", "Du ma may!", "Dit me may!"]
pos_comments = ["Good work!!!!!!!", "Wow, you're cool", "Amazing job!!", "Nice hit!", "Great reaction!", "Keep it up!", "Excellent!!!!!", "Youre kilin it!", "You>>John", ":D <3"]