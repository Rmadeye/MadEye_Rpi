# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:34:30 2019

@author: Rafcio
"""
import RPi.GPIO as GPIO

def set_alarm():
    while True:
       GPIO.output(18,0) # Buzzer on - ALARM LOUD
       GPIO.output(21.0) # Socket on - POWER DOWN
       