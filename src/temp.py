import w1thermsensor, time
import RPi.GPIO as GPIO


class TempControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)


    def check_temperature(self):

        sensor = w1thermsensor.W1ThermSensor()
        temp = sensor.get_temperature()

        if temp < 35:

            pass

        if temp > 35 and temp <50:
            GPIO.setup(21, GPIO.OUT)
            time.sleep(0.5)
            GPIO.output(21, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.setup(21, GPIO.OUT)
            time.sleep(0.5)
            GPIO.output(21, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.setup(21, GPIO.OUT)
            time.sleep(0.5)
            GPIO.output(21, GPIO.HIGH)

        if temp > 50:
            GPIO.setup(21, GPIO.OUT)
            time.sleep(3)
            GPIO.output(21, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.setup(21, GPIO.OUT)
            time.sleep(0.2)
            GPIO.output(21, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.setup(21, GPIO.OUT)
            time.sleep(0.2)
            GPIO.output(21, GPIO.HIGH)








