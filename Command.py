from src import driver, temp
import time, RPi.GPIO

if __name__ == "__main__":
    drive = driver.Driver()
    temp_history = []
    try:
        while True:
            time.sleep(1)
            drive.collect_data()
            # temp_history.append(float(temp.TempControl().check_temperature()))

    except:
        print("Error occured")
    finally:
        RPi.GPIO.cleanup()
