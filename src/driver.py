# -*- coding: utf-8 -*-
"""
Python driver for raspberry temperature sensor
"""

from src import temp as t
import RPi.GPIO as GPIO
import time, datetime
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
        distilled_temp = self.temp_driver.check_distill_temp()
        # inner_temp = int(self.temp_driver.check_inner_temp())
        return self.warnings(distilled_temp)

    def warnings(self,temp):#,outflow):
        if temp <30:
            GPIO.output(26, 1)
            print(Fore.GREEN +"Current time: {}, \nCurrent distillate temperature: {}".format
            (datetime.datetime.now().strftime('%H:%M:%S'),
             round(float(temp), 1)))


        if temp>30:
            GPIO.output(26, 0)
            time.sleep(0.5)
            GPIO.output(26, 1)
            print(Fore.YELLOW + "Current time: {}, \nCurrent distillate temperature: {}".format(
                datetime.datetime.now().strftime('%H:%M:%S'),
                round(float(temp), 1)))


        if temp >35:
            print("WARNING! Temperature too high!")
            print(Fore.RED + "Current time: {}, \nCurrent distillate temperature: {}".format(
                datetime.datetime.now().strftime('%H:%M:%S'),
                round(float(temp), 1)))
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(0.25)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
            time.sleep(0.25)
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(0.25)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
            time.sleep(0.25)
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(0.25)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD

        if temp>45:
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(5)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
            time.sleep(0.1)
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
    #
    # def actual_dis_temp(self, temp):
    #     if temp > 70:
    #         print(Fore.GREEN + "Current inner temperature: {} Celsius".format(round(float(temp), 1)))
    #
    #     if temp >96:
    #         GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
    #         time.sleep(0.25)
    #         GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
    #         time.sleep(0.25)
    #         GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
    #         time.sleep(0.25)
    #         GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
    #         time.sleep(0.25)
    #         GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
    #         time.sleep(2)
    #         GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
    #         time.sleep(20)
    #         print(Fore.CYAN + "Current inner temperature: {} Celsius".format(round(float(temp), 1)))
    #         print("That's it")




