# -*- coding: utf-8 -*-
"""
Python driver for raspberry temperature sensor
"""

import datetime
import smtplib
from src import temp as t
#import flowmeter as f
import RPi.GPIO as GPIO
import time

class Driver:
    def __init__(self):
        print("Initializing")
        self.temp_driver = t.TempControl()
        GPIO.setmode(GPIO.BCM)
        #GPIO.setup(18, GPIO.OUT) # Diode online
        GPIO.setup(21, GPIO.OUT) # Buzzer online
        GPIO.setup(4, GPIO.OUT) # W1 online
        GPIO.setup(19, GPIO.OUT) # Check temp diode online
        GPIO.output(21,0)

        time.sleep(0.2)
        GPIO.output(21,1)
        GPIO.output(4,1)



    def collect_data(self):
        log=open("log.txt","a+")
        current_temp = int(self.temp_driver.check_temperature())
    #    outflow=f.collect_flow()
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log.write(time +" Temperature: "+ str(current_temp)+"\xb0C"+"\n")
        log.close()
        return self.warnings(current_temp)

    def warnings(self,temp):#,outflow):
        if temp <30:
            GPIO.output(19, 1)

        # elif temp>30:
        #     GPIO.output(19, 0)


        elif temp >40:
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

        elif temp>55:
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
            time.sleep(5)
            GPIO.output(21, 1)  # Buzzer on - ALARM LOUD
            time.sleep(0.1)
            GPIO.output(21, 0)  # Buzzer on - ALARM LOUD
        


