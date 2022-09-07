import RPi.GPIO as GPIO
import sys
import time
import pymysql
from Adafruit_AMG88xx import Adafruit_AMG88xx

sensor = Adafruit_AMG88xx(busnum=1)

#db 연동/연결하기 
conn = pymysql.connect(host="192.168.1.164",user="raspi_inae",passwd="12341234",db="sensor")

#host : ip주소
#user : user_name 
#passwd : password 
#db : database_name 

try :

     #db 접속 
     with conn.cursor() as cur:

        while True :
    
            temperature = sensor.readThermistor()
            #temperature : amg8833에서 불러온 온도값 
          
            if temperature is not None:
                print('temp=%0.2f',temperature)
                print(type(temperature))
                
                #db 삽입
                cur.execute("insert into thermal (date, temperature) values(default, {0:0.2f})".format(temperature))
                conn.commit()
                
                #thermal 테이블에 date(날짜), tenmperature(float형식)값 추가하기 
               
               
            else:
                print("Failed to get reading.")
            time.sleep(3)
            #3초 간격으로 반복 
               
except KeyboardInterrupt :
       exit()
finally:
       conn.close()
