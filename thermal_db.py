import RPi.GPIO as GPIO
import sys
import time
import pymysql
from Adafruit_AMG88xx import Adafruit_AMG88xx

sensor = Adafruit_AMG88xx(busnum=1)
conn = pymysql.connect(host="192.168.1.164",user="raspi_inae",passwd="12341234",db="sensor")

try :
     with conn.cursor() as cur:

        while True :

            temperature = sensor.readThermistor()
            
            if temperature is not None:
                print('temp=%0.2f',temperature)
                print(type(temperature))

                cur.execute("insert into thermal (date, temperature) values(default, {0:0.2f})".format(temperature))
                conn.commit()
            else:
                print("Failed to get reading.")
            time.sleep(3)

except KeyboardInterrupt :
       exit()
finally:
       conn.close()
