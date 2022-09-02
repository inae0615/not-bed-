
print("테스트 파일입니다.")

while (1):

  abc= input('침대에 사람이 있나요?(yes/no) :')

  if abc == 'no' or abc == 'NO':
    #카카오톡 자동실행 코드 구현
    exec(open("app.py").read())
    print("test 성공")

  elif abc == 'yes' or abc == 'YES':

    print("사람이 있군요")

  else:
    print("잘못입력하셨습니다.")











































