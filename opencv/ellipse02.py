import numpy as np
import cv2 as cv


# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 500
height = 500
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)


center = (int(height/2), int(width/2))


# center를 중심으로 하는 3개의 원을 그립니다.

# x축 방향 반지름 길이 10, y축 방향 반지름 길이 200인 녹색 타원을 그립니다.
# 수직선에 가까운 타원이 그려집니다.       green
cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3 )

# 타원을 시계방향으로 45도 회전하여 그립니다.     red
cv.ellipse(img, center, (10, 200), 45, 0, 360,  (0, 0, 255), 3 )

# 타원을 반시계방향으로 45도 회전하여 그립니다.    blue
cv.ellipse(img, center, (10, 200), -45, 0, 360,  (255, 0, 0), 3 )


cv.imshow("result", img)
cv.waitKey(0);