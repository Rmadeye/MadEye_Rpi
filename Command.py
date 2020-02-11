from src import driver
import time, RPi.GPIO

if __name__ == "__main__":
    drive = driver.Driver()
    try:
        while True:
            time.sleep(1)
            drive.collect_data()
    except:
        print("Error occured")
    finally:
        RPi.GPIO.cleanup()
