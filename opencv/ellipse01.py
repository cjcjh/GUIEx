import numpy as np
import cv2 as cv

# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 500
height = 500
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

center = (int(height/2), int(width/2))

# center를 중심으로 하는 3개의 원을 그립니다.

# x축 방향 반지름 길이 200, y축 방향 반지름 길이 10인 파란색 타원을 그립니다.
cv.ellipse(img, center, (200, 10), 0, 0, 360, (255, 0, 0), 3 )
# x축 방향 반지름 길이 10, y축 방향 반지름 길이 200인 녹색 타원을 그립니다.
cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3 )
# x축 방향 반지름 길이 200, y축 방향 반지름 길이 200인 빨간색 타원을 그립니다.
# 반지름 200인 원이 그려집니다.
cv.ellipse(img, center, (200, 200), 0, 0, 360, (0, 0, 255), 3 )

cv.imshow("result", img)
cv.waitKey(0);