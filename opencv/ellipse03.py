import numpy as np
import cv2 as cv

# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 500
height = 500
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

center = (int(height/2), int(width/2))

# 타원을 시계방향으로 0도에서 90도까지만 그립니다.
cv.ellipse(img, center, (100, 100), 0, 0, 90,  (0, 0, 255), 3 )
#cv.ellipse(img, center, (x, y길이), 시작할각도, (모르겠음), 0도부터 그리는각도, 색깔, 사이즈)

cv.imshow("result", img)
cv.waitKey(0);