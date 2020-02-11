import w1thermsensor, time
import RPi.GPIO as GPIO


class TempControl:
    def __init__(self):
        GPIO.setwarnings(False)


    def check_temperature(self):

        sensor = w1thermsensor.W1ThermSensor()
        temp = sensor.get_temperature()
        print(round(float(temp)),1)

        return temp






