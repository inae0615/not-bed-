# Team: not-bed

project_1

IOT3_Class

from.한직교_안산

-욕창방지 침대 만들기  

----------------------------------------------
What I do

1. 영상처리
- 침대 유무/ yolov5를 이용하여 침대 학습
- 침대 학습된 결과를 토대로 실시간 검출
- 열화상 카메라 띄움

2. 백엔드
- 아파치+마리아db설치 및 grafana 연동 
- flask및 mjpg를 활용하여 웹캠영상을 ip로 띄우는 cctv 만듦
- yolov5를 활용해 cctv의 실시간 검출된 결과값(yp, np)을 db에 저장하고 대시보드에 띄움
- 열화상카메라에서 얻은 온도센서값을 db에 저장하여 대시보드 띄움
- 카카오톡 나에게 메세지 보내기 코드를 수정, 보완하여 전송된 내역을 db에 저장하여 대시보드 띄움 

3. 모터
- pca9685모듈을 이용하여 python으로 서브모터 제어하는 코드 작성 
