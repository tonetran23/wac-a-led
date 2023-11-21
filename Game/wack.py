#!/usr/bin/python
# Author: Tony Tran and Brandon Vu

import random
from time import sleep
from .constants import *
from .lcd import *
from threading import Timer, Thread
from datetime import datetime, timedelta

class Wack(Thread):
    def __init__(self):
        super().__init__()
        self.start_game = True
        self.time1 = 1
        self.time2 = 0
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0
        self.score = 0
        self.comment = None
        self.led_on = False
        self.led = None
        self.btn_a = btn_1
        self.btn_b = btn_2
        self.btn_c = btn_3
        self.btn_d = btn_4
        self.early = False
        
    def run(self):
        #self.reset_led()
        self.lcd_score()
        self.rad_led()
    
    def lcd_score(self):
        if not GPIO.input(self.btn_a) and self.led_on and self.start_game: # Updates score if button is pressed and correct led is on
            self.score += 1
            self.comment = random.randrange(0,9,1)
            lcd_string("Score: " + str(self.score), LCD_LINE_1)
            lcd_string(pos_comments[self.comment], LCD_LINE_2)
            sleep(1)
        Timer(0.1, self.lcd_score).start()

    def rad_led(self):
        if self.start_game:
            self.time1 = random.randrange(1, 3, 1)
            self.time2 = random.randrange(1, 3, 1)
            self.led = random.choice([led_1, led_2, led_3, led_4])
            
            # Sets correct leds to correct buttons
            if self.led == led_1:
                self.btn_a = btn_1
                self.btn_b = btn_2
                self.btn_c = btn_3
                self.btn_d = btn_4
            if self.led == led_2:
                self.btn_a = btn_2
                self.btn_b = btn_1
                self.btn_c = btn_3
                self.btn_d = btn_4
            if self.led == led_3:
                self.btn_a = btn_3
                self.btn_b = btn_1
                self.btn_c = btn_2
                self.btn_d = btn_4
            if self.led == led_4:
                self.btn_a = btn_4
                self.btn_b = btn_1
                self.btn_c = btn_2
                self.btn_d = btn_3
            
            self.start_time = datetime.now()
            while self.elapsed_time < self.time2:
                self.end_time = datetime.now()
                self.elapsed_time = (self.end_time - self.start_time).total_seconds()
            
                # Detects if any of the buttons are pressed before the correct LED is lit up
                if not GPIO.input(self.btn_a) or not GPIO.input(self.btn_b) or not GPIO.input(self.btn_c) or not GPIO.input(self.btn_d):
                    self.early = True
                    break
            self.elapsed_time = 0
            
            # Lights up correct LED if no buttons were pressed before
            if not self.early:
                GPIO.output(self.led, 1)
                self.led_on = True
                
                # Measures the amount of time the LED has been on and compares it to the random time assigned to the duration that the LED should remain on
                self.start_time = datetime.now()
                while GPIO.input(self.btn_a) and self.elapsed_time < self.time1 and GPIO.input(self.btn_b) and GPIO.input(self.btn_c) and GPIO.input(self.btn_d):
                    self.end_time = datetime.now()
                    self.elapsed_time = (self.end_time - self.start_time).total_seconds()
                
                # After either a button is pressed or the amount of time the LED has been on exceeds the alotted time it should remain on, the next line will run
            
            # Displays a negative comment and stops the game if either the wrong button was pressed or the amount of time the LED has been on exceeds the alotted time it should remain on
            if self.elapsed_time >= self.time1 or not GPIO.input(self.btn_b) or not GPIO.input(self.btn_c) or not GPIO.input(self.btn_d) or self.early:
                self.comment = random.randrange(0,9,1)
                lcd_string("Score: " + str(self.score), LCD_LINE_1)
                lcd_string(neg_comments[self.comment], LCD_LINE_2)
                print("LOSER! Press Ctrl+c to exit")
                self.start_game = False
            
            # Turns off LED and continues game if the correct button was pressed
            GPIO.output(self.led, 0)
            sleep(0.2)
            self.led_on = False
            self.elapsed_time = 0
            
            # Detects if the game is still continuing, then flashes LEDs
            if self.start_game:
                self.correct()
                
            # Detects if the game is over, then plays buzzer
            if not self.start_game:
                GPIO.output(buz, 1)
                sleep(2)
                GPIO.output(buz, 0)
        Timer(0.1, self.rad_led).start()
    
    def reset_led(self):
        GPIO.output(led_1, 0)
        GPIO.output(led_2, 0)
        GPIO.output(led_3, 0)
        GPIO.output(led_4, 0)
        
    def game_end(self):
        return self.start_game
    
    def correct(self):
        GPIO.output(led_1, 1)
        GPIO.output(led_2, 1)
        GPIO.output(led_3, 1)
        GPIO.output(led_4, 1)
        GPIO.output(buz, 1)
        sleep(0.2)
        GPIO.output(led_1, 0)
        GPIO.output(led_2, 0)
        GPIO.output(led_3, 0)
        GPIO.output(led_4, 0)
        GPIO.output(buz, 0)
        sleep(0.1)
        GPIO.output(led_1, 1)
        GPIO.output(led_2, 1)
        GPIO.output(led_3, 1)
        GPIO.output(led_4, 1)
        GPIO.output(buz, 1)
        sleep(0.2)
        GPIO.output(led_1, 0)
        GPIO.output(led_2, 0)
        GPIO.output(led_3, 0)
        GPIO.output(led_4, 0)
        GPIO.output(buz, 0)
        sleep(0.1)
        GPIO.output(led_1, 1)
        GPIO.output(led_2, 1)
        GPIO.output(led_3, 1)
        GPIO.output(led_4, 1)
        GPIO.output(buz, 1)
        sleep(0.2)
        GPIO.output(led_1, 0)
        GPIO.output(led_2, 0)
        GPIO.output(led_3, 0)
        GPIO.output(led_4, 0)
        GPIO.output(buz, 0)