from socket import AddressFamily
import time
import requests
import json
import pymysql

def sandmsg():
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

g_name = '이인애'
p_name = '김철수'
p_room = '504'

in_hour = input("시간을 입력하세요.(숫자만입력, 몇 시간?) :")
in_min = input("분을 입력하세요.(숫자만입력, 몇 분?) :")
in_sec = input("초를 입력하세요.(숫자만입력, 몇 초?) :")
smin = int(in_min)*60
shour = int(in_hour)*smin
sec = shour + smin + int(in_sec)
print(sec)

#while은 반복문으로 sec가 0이 되면 반복을 멈춰라
while (sec != 0) :
    sec = sec-1
    time.sleep(1)
    print(sec)
    if sec <= 0 :
        sandmsg()

print("카카오톡 전송완료")

conn = pymysql.connect(host="192.168.1.164",user="raspi_inae",passwd="12341234",db="kakao")
cur = conn.cursor()
cur.execute("insert into message (date, patient_name, p_room, guardian_name) values(default, '''{0}''','''{1}''','''{2}''')".format(p_name,p_room,g_name))
conn.commit()
time.sleep(1)
conn.close()

print("db 전송완료 ")

#while (sec != 0) :
#        sec = sec-1
#        time.sleep(1)
#        print(sec)
#        break
#    if sec > 0 :
#        elif sec <= 0 :
#            sandmsg()
#    else :
#        print('error')
