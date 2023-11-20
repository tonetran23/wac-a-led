#!usr/bin/python
#Authors: Tony Tran and Brandon Vu

from .constants import *
from .lcd import *
from threading import Timer, Thread
import time
import random
from datetime import datetime, timedelta

class Lcd(Thread):
    # Initialize all variables
    def __init__(self):
        super().__init__()
        self.start_game = False
        self.end_game = False
        self.score = 0
        self.ran = None
        self.led_on = True
        self.time1 = None
        self.time2 = None
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0

    # Overload Thread.run
    def run(self):
        lcd_setup()
        lcd_init()
        self.btn_monitor()
        while not self.start_game:
            lcd_string("Press 1 for Wack", LCD_LINE_1)
            lcd_string("Press 2 to xxxx", LCD_LINE_2)
            time.sleep(1)
            lcd_string("Press 3 to xxxx", LCD_LINE_1)
            lcd_string("Press 4 to xxxx", LCD_LINE_2)
            time.sleep(1)
        lcd_string("Score: " + str(self.score), LCD_LINE_1)
        lcd_string("Starting in 3", LCD_LINE_2)
        time.sleep(1)
        lcd_string("Starting in 2", LCD_LINE_2)
        time.sleep(1)
        lcd_string("Starting in 1", LCD_LINE_2)
        time.sleep(1)
        lcd_string("Wack-a-LED!", LCD_LINE_2)
        self.lcd_score()
        self.led_rad()
        
    # Periodic function to monitor button press
    def btn_monitor(self):
        if not self.start_game:
            if not GPIO.input(btn_1):
                self.start_game = True
                return
            Timer(0.1, self.btn_monitor).start()
    
    # LCD update score on display
    def lcd_score(self):
        if not GPIO.input(btn_1) and self.led_on and self.start_game: # Updates score if button is pressed and correct led is on
            self.score += 1
            self.ran = random.randrange(0,9,1)
            lcd_string("Score: " + str(self.score), LCD_LINE_1)
            lcd_string(pos_comments[self.ran], LCD_LINE_2)
            time.sleep(1)
        Timer(0.1, self.lcd_score).start()
    
    # Turns on LED randomly
    def led_rad(self):
        if self.start_game:
            self.time1 = random.randrange(1, 3, 1)
            self.time2 = random.randrange(1, 3, 1)
            time.sleep(self.time2)
            GPIO.output(ledtest, 1)
            self.led_on = True
            self.start_time = datetime.now()
            while GPIO.input(btn_1) and self.elapsed_time < self.time1:
                self.end_time = datetime.now()
                self.elapsed_time = (self.end_time - self.start_time).total_seconds()
            pass
            if self.elapsed_time >= self.time1:
                self.ran = random.randrange(0,9,1)
                lcd_string("Score: " + str(self.score), LCD_LINE_1)
                lcd_string(neg_comments[self.ran], LCD_LINE_2)
                self.start_game = False
            GPIO.output(ledtest, 0)
            time.sleep(0.1)
            self.led_on = False
            self.elapsed_time = 0
        Timer(0.1, self.led_rad).start()