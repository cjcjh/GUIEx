# 0302.py
import cv2
import numpy as np

img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
# 배열 모두 0 unit8
x1, x2 = 100, 400
y1, y2 = 100, 400
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255)) # 사각형 그려

pt1 = 120, 50
pt2 = 300, 500
cv2.line(img, pt1, pt2, (255,0,0), 2)  # 줄 그려

imgRect = (x1, y1, x2-x1, y2-y1)
# imgRect =
retval, rpt1, rpt2 = cv2.clipLine(imgRect, pt1, pt2)
# cv2.clipLine(검출하려는 직사각형 영역, 직선의 시작점, 직선의 종료점)
# retval(결과) : True 사각형 내에 선이 있음, False : 사각형 내에 선이 없음
# rpt1 : 사각형 안에 있는 선의 시작점
# rpt2 : 사각형 안에 있는 선의 종료점

if retval:
    cv2.circle(img, rpt1, radius=50, color=(0, 255, 0), thickness=-1)
    cv2.circle(img, rpt2, radius=5, color=(0, 255, 0), thickness=-1)
    # circle(원이 그려질 이미지, 원의중심좌표 , 반지름, 색상, 두께, lineType, shift)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()