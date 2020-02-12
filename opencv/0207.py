# 0207.py
import cv2

##cap = cv2.VideoCapture(0)  # 0번 카메라, device or filename
cap = cv2.VideoCapture('./data/video2.avi')  # avi 파일
## cv2.VideoCapture :
## 1 : 카메라번호
## 2 : filename
## 3 : protocol(ip:port, url)
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# cv2 속성들
# cv2.CAP_PROP_FRAME_WIDTH	프레임의 너비	-
# cv2.CAP_PROP_FRAME_HEIGHT	프레임의 높이	-
# cv2.CAP_PROP_FRAME_COUNT	프레임의 총 개수	-
# cv2.CAP_PROP_FPS	프레임 속도	-
# cv2.CAP_PROP_FOURCC	코덱 코드	-
# cv2.CAP_PROP_BRIGHTNESS	이미지 밝기	카메라만 해당
# cv2.CAP_PROP_CONTRAST	이미지 대비	    카메라만 해당
# cv2.CAP_PROP_SATURATION	이미지 채도	카메라만 해당
# cv2.CAP_PROP_HUE	이미지 색상	        카메라만 해당
# cv2.CAP_PROP_GAIN	이미지 게인	        카메라만 해당
# cv2.CAP_PROP_EXPOSURE	이미지 노출	    카메라만 해당
# cv2.CAP_PROP_POS_MSEC	프레임 재생 시간	ms 반환
# cv2.CAP_PROP_POS_FRAMES	현재 프레임	프레임의 총 개수 미만
# CAP_PROP_POS_AVI_RATIO	비디오 파일 상대 위치	0 = 시작, 1 = 끝

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

str = "actual forcc format: " + decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
print (str)
print(hex(int(cap.get(cv2.CAP_PROP_FOURCC))))

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# frame_size 캡한 가로새로 사이즈 정해주기
print(type(frame_size))
print('frame_size =', frame_size)
"""
while True:
    retval, frame = cap.read()  # 프레임 캡처
    if not retval:
        break

    cv2.imshow('filename', frame)

    key = cv2.waitKey(25) # waitkey 설정
    if key == 27:  # Esc 입력시 imshow 브레이크
        break

if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
"""
while(cap.isOpened()):
    retval, frame = cap.read()  # 프레임 캡처 한 값 : retval
    if not retval:
        break

    cv2.imshow('filename', frame)  # 파일 프레임대로 보여주기

    print(cap.get(cv2.CAP_PROP_POS_MSEC))
    key = cv2.waitKey(25) # waitkey 설정
    if key == 27:  # Esc 입력시 imshow 브레이크
        break

#if cap.isOpened():
cap.release()
cv2.destroyAllWindows()
