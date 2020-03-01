import w1thermsensor
import RPi.GPIO as GPIO




class TempControl:
    def __init__(self):
        GPIO.setwarnings(False)


    def check_distill_temp(self):

        sensor = w1thermsensor.W1ThermSensor()
        temp_distilled = sensor.get_temperature()

        return temp_distilled
    #
    # def check_inner_temp(self):
    #     sensor = w1thermsensor.W1ThermSensor()
    #     temp_inner = sensor.get_temperature()
    #
    #     return temp_inner






