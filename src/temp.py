import w1thermsensor


class TempControl:
    def __init__(self):
        pass


    def read_temperature(self):

        sensor = w1thermsensor.W1ThermSensor()
        temp = sensor.get_temperature()
        print(str(temp))
        return temp


