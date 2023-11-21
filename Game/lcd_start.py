#!usr/bin/python
#Authors: Tony Tran and Brandon Vu

from .constants import *
from .lcd import *
from threading import Timer, Thread
from time import sleep
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
        self.wack_start = False

    # Overload Thread.run
    def run(self):
        pin_setup()
        lcd_init()
        self.btn_monitor()
        while not self.start_game:
            if not self.end_game:
                lcd_string("Press 1 for Wack", LCD_LINE_1)
                lcd_string("Press 2 to xxxx", LCD_LINE_2)
                sleep(1)
                lcd_string("Press 3 to xxxx", LCD_LINE_1)
                lcd_string("Press 4 to xxxx", LCD_LINE_2)
                sleep(1)
            if self.end_game:
                lcd_string("Quitting Game...", LCD_LINE_1)
                lcd_string("See'ya next time", LCD_LINE_2)
        lcd_string("Score: " + str(self.score), LCD_LINE_1)
        lcd_string("Starting in 3", LCD_LINE_2)
        sleep(1)
        lcd_string("Starting in 2", LCD_LINE_2)
        sleep(1)
        lcd_string("Starting in 1", LCD_LINE_2)
        sleep(1)
        lcd_string("Wack-a-LED!", LCD_LINE_2)
        self.wack_start = True
        
    # Periodic function to monitor button press
    def btn_monitor(self):
        if not self.start_game and not self.end_game:
            if not GPIO.input(btn_1):
                self.start_game = True
                return
            if not GPIO.input(btn_2) or not GPIO.input(btn_3) or not GPIO.input(btn_4):
                self.end_game = True
                return
            Timer(0.1, self.btn_monitor).start()

    # Function to start wack
    def start_wack(self):
        return self.wack_start
        
    def game_end(self):
        return self.end_game