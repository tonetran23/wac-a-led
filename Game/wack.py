#!/usr/bin/python

# description:
#    LED ligths at random
#    all LEDs blink after successful hit
# Author: Tony Tran and Brandon Vu

import random
from constants import *

class wack(thread):
    def __init__(self):
        self.wack_led_pattern = True
        self.moniter_button = False
        self.buzzer = False
        
        
    def run(self):
        moniter_button
       
       
    def moniter_button(self):
        try:
            while (1):
                if not GPIO.input(btn_1) == 1:
            
                if not GPIO.input(btn_2) == 1:
            
                if not GPIO.input(btn_3) == 1:
           
                if not GPIO.input(btn_4) == 1:
               
    def wack_led_pattern(self):
        list_led = [led_1, led_2, led_3, led_4]
        try:
            GIPO.output(random.choice(list_led), 1)
            
    
    
