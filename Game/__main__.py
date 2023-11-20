#!/usr/bin/python

# description:
# select mode
# Author: Tony Tran and Brandon Vu

from .constants import *
from .lcd_start import Lcd
from .lcd import *
from .wack import Wack

def main():
    try:
        print("Running...")
        lcd = Lcd()
        lcd.start()
        #wack = Wack()
        #wack.start()
    
    except KeyboardInterrupt:
        if lcd is not None:
            lcd.stop()
        print()
        print("Ctrl+c pressed, exiting")
    
    finally:
        pass

if __name__ == "__main__":
    main()