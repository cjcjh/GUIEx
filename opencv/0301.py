#0301.py
import cv2
import numpy as np

# White 배경 생성
img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# zeris = 해당배열에 모두 0을 집어 넣음
#img = np.ones((512,512,3), np.uint8) * 255
# ones = 해당배열에 모두 1을 집어 넣음
#img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
# 배열에 사용자가 지정한 값을 넣어줌
#img = np.zeros((512,512, 3), np.uint8)
# Black 배경
#img = np.eye(512, 512, 3)
# eye 대각선 그리기
pt1 = 100, 100
pt2 = 400, 400
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
#cv2.rectangle(이미지, x, y, 색깔, 사이즈)

cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)
#cv2.line(이미지, x, y, 색깔, 사이즈)
cv2.line(img, (0, 0), (0, 500), (0,0,255), 5)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
