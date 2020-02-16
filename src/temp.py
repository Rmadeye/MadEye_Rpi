import w1thermsensor, time, datetime
import RPi.GPIO as GPIO


class TempControl:
    def __init__(self):
        GPIO.setwarnings(False)


    def check_temperature(self):

        sensor = w1thermsensor.W1ThermSensor()
        temp = sensor.get_temperature()
        time=datetime.datetime.now().strftime('%H:%M:%S')
        print("Current time: {}, \n Current temperature: {}".format(time, round(float(temp), 1)))

        return temp






