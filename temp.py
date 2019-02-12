# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:49:09 2019

@author: Rafcio
"""
#@import w1thermsensor
def read_temperature():
    sensor = open("odczyt.txt",'r')
#    sensor = w1thermsensor.W1ThermSensor()
    temp=int(sensor.read().strip())
#    temp = sensor.get_temperature()
    print(str(temp))
    return temp
#read_temperature()