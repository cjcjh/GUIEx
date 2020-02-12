# 0210.py
import cv2

cap = cv2.VideoCapture('./data/vtest.avi')  # 0번 카메라
#cap = cv2.VideoCapture(0)  # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

# fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# cv2.VideoWriter(outputFile, fourcc, frame, frame_size, isColor)
#           outputFile (str) – 저장될 파일명
#           fourcc – frame 압축관련 4자리 code. cv2.VideoWriter_fourcc()한거
#           frame (float) – 초당 저장될 frame
#           size (list) – 저장될 사이즈(ex; 640, 480)
#           isColor - 컬러 저장 여부
# fourcc(*'MJPG', *'DIVX', *'XVID')
out1 = cv2.VideoWriter('./data/record2.avi', fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter('./data/record3.avi', fourcc, 20.0, frame_size, isColor=False)

while True:
    retval, frame = cap.read()
    if not retval:
        break
    out1.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    key = cv2.waitKey(25)
    if key == 27:
        break
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
