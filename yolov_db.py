#yolov
#detect.py_일부발췌  
#162 줄/

import time
import pymysql

 # Write results

                    for *xyxy, conf, cls in reversed(det):                                  
                    db_name = names[int(c)] #db_name : np or yp
                    percent = float(conf)   #percent : 확률 
                    
                    #db 연동/연결                         
                    conn = pymysql.connect(host="192.168.1.164",user="raspi_inae",passwd="12341234",db="yolov5")
                    #host : ip주소
                    #user : user_name 
                    #passwd : password 
                    #db : database_name 

                    cur = conn.cursor() #db 접속
                    cur.execute("insert into detect (date, name, conf) values(default, '''{0}''', {1:0.5f})".format(db_name, percent))
                    #detect 테이블에 date(날짜), db_name, 확률 값 추가하기 
                            
                    conn.commit()
                    time.sleep(0) #딜레이 0 
                                    
 
                    #검출 결과에 따른 카카오톡 자동 전송 
                    cnt = 0 
                    while(1):
                        if db_name == 'np' and percent >= 0.8 and cnt == 0:
                            exec(open("app.py").read()) #카카오톡 자동 실행파일 불러오기 
                            print("{0:0.3f}% 확률로 침대에 사람이 없습니다".format(percent*100))
                            cnt = 1
 
                        elif db_name == 'yp':
                            print("{0:0.3f}% 확률로 침대에 사람이 있습니다".format(percent*100))
                            cnt = 0
                            break

                        elif db_name == 'np' and percent < 0.8:
                            print("{0:0.3f}% 확률로 침대에 사람이 없을 수도 있습니다.".format(percent*100))
                            cnt = 0
                            break



