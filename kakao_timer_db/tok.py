import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = '60656af69143d4b0aa9d6f67e528a26e'
redirect_uri = 'https://example.com/oauth'
code ='372-EcjBlGeRToftR2qpNPWtCg_lJTRZodZ5WTxwQpshwhDBKMkjnYh4ZLuG4m4r2qanhwopb1QAAAGC_JAdDg'

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)
