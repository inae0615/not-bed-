from socket import AddressFamily
import time
import requests
import json
import pymysql

def sendmsg():
    #발행한 토큰 불러오기
    with open("token.json","r") as kakao:
        tokens = json.load(kakao)
    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers= {"Authorization" : "Bearer " + tokens["access_token"]}

    data = {
        'object_type': 'text',
        'text': g_name+'님, '+p_name+' 환자의 상태를 확인해 주세요',
        'link': {
            'web_url': 'https://developers.kakao.com',
            'mobile_web_url': 'https://developers.kakao.com'
        },
        'button_title': '키워드'
    }

    data = {'template_object': json.dumps(data)}
    response = requests.post(url, headers=headers, data=data)
    response.status_code

g_name = '이인애'  #보호자 이름
p_name = '김철수'  #환자 이름
p_room = '504'   #병실 


#타이머 입력  
in_hour = input("시간을 입력하세요.(숫자만입력, 몇 시간?) :")
in_min = input("분을 입력하세요.(숫자만입력, 몇 분?) :")
in_sec = input("초를 입력하세요.(숫자만입력, 몇 초?) :")
smin = int(in_min)*60
shour = int(in_hour)*smin
sec = shour + smin + int(in_sec)
print(sec)

#sec가 0이 되면 반복을 멈추고 카카오톡 메세지 보내는 함수 호출 
while (sec != 0) :
    sec = sec-1
    time.sleep(1)
    print(sec)
    if sec <= 0 :
        sendmsg()

print("카카오톡 전송완료") #카톡 전송확인 

#db 연동/연결 
conn = pymysql.connect(host="192.168.1.164",user="raspi_inae",passwd="12341234",db="kakao")
#host : ip주소
#user : user_name 
#passwd : password 
#db : database_name 

cur = conn.cursor() #db 접속 
cur.execute("insert into message (date, patient_name, p_room, guardian_name) values(default, '''{0}''','''{1}''','''{2}''')".format(p_name,p_room,g_name))
# messgae 테이블에 date, patient_name, p_room, guardian_name 값 추가/ 삽입하기 


conn.commit()
time.sleep(1)
conn.close()  #db_종료 

print("db 전송완료 ")  #db 전송확인 
