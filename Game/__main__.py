#!/usr/bin/python

# description:
# select mode
# Author: Tony Tran and Brandon Vu

from .constants import *
from .lcd_start import Lcd
from .lcd import *
from .wack import Wack
from time import sleep
import sys

def main():
    try:
        print("Running...")
        lcd = Lcd()
        lcd.start()
        while not lcd.game_end():
            if lcd.start_wack():
                break
            sleep(0.1)
        if lcd.game_end():
            print("Quitting Game")
            exit()
        wack = Wack()
        wack.start()
        while wack.game_end():
            sleep(1)
    
    except KeyboardInterrupt:
        print()
        print("Ctrl+c pressed, exiting")
    
    finally:
        leds_off()
        exit()

if __name__ == "__main__":
    main()