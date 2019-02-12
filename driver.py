# -*- coding: utf-8 -*-
"""
Python driver for raspberry temperature sensor
"""
import datetime
import smtplib
import temp as t
#import flowmeter as f
#import alarm_socket as alarm
#import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT) # Buzzer online
#GPIO.setup(21, GPIO.OUT) # Socket online
#GPIO.setup(20, GPIO.OUT) # Diode online
#GPIO.output(20,1)
server = smtplib.SMTP('smtp.p.lodz.pl', 587)

def collect_data():
    log=open("log.txt","a+")
    thist=int(t.read_temperature())
#    outflow=f.collect_flow()
    time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time)
    log.write(time +" Temperature: "+ str(thist)+"\xb0C"+"\n")
    log.close()
    return thist#,outflow

def warnings(temp):#,outflow):
    if temp <20:
        print("WARNING! temperature too low!")
        warlow="WARNING! temperature too low!"
        server.sendmail("800833@edu.p.lodz.pl","800833@edu.p.lodz.pl",warlow)
        server.quit()
  #     alarm.set_alarm()
    elif temp >50:
        print("WARNING! Temperature too high!")
        warhigh="WARNING! Temperature too high!"
        server.sendmail("800833@edu.p.lodz.pl","800833@edu.p.lodz.pl",warhigh)
        server.quit()
   #     alarm.set_alarm()
#    elif outflow ==0:
#        print("WARNING! Pressure drop!")
#       pressdrop="WARNING! Pressure drop!"
        #server.sendmail("800833@edu.p.lodz.pl","800833@edu.p.lodz.pl",pressdrop)
        #server.quit()
    else:
        server.quit()
        
    
    
def main(): 
    server.starttls()
    server.login("800833@edu.p.lodz.pl", input("Haslo:"))
    collect_data()
    warnings(t.read_temperature())#,f.collect_flow())           
    while True:
        time.sleep(600)
        main()

main()



