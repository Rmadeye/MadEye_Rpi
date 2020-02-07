from src import driver
import time

if __name__ == "__main__":
    drive = driver.Driver()
    while True:
        time.sleep(1)
        drive.collect_data()


