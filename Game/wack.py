#!/usr/bin/python

# description:
#    LED ligths at random
#    all LEDs blink after successful hit
# Author: Tony Tran and Brandon Vu

import random
import time
from .constants import *
from threading import Timer, Thread

class Wack(Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            print('hello')
            time.sleep(1)