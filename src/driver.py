# -*- coding: utf-8 -*-
"""
Python driver for raspberry temperature sensor
"""

from src import temp as t
import RPi.GPIO as GPIO
import time
import colorama
from colorama import Fore, Style


class Driver:
    def __init__(self):
        print(Fore.GREEN + "Initializing")
        self.temp_driver = t.TempControl()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT) # Buzzer online
        GPIO.setup(26, GPIO.OUT) # Check temp diode online
        GPIO.output(21,0)

        time.sleep(0.2)
        GPIO.output(21,1)


#27603881
    def collect_data(self):
        current_temp = int(self.temp_driver.check_temperature())
        return self.warnings(current_temp)

    def warnings(self,temp):#,outflow):
        if temp <30:
            GPIO.output(26, 1)

        if temp>30:
            GPIO.output(26, 0)

        if temp >35:
            print("WARNING! Temperature too high!")
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(0.5)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
            time.sleep(0.5)
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(0.5)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
            time.sleep(0.5)
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(0.5)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD

        if temp>45:
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(5)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
            time.sleep(0.1)
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
        


