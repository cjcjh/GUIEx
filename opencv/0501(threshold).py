# 0501.py

import cv2
import numpy as np
src = cv2.imread('./data/heart10.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src',  src)

ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)
#cv2.threshold(src, thresh, maxval, type)
#src = input image로 single-channel 이미지(grayscale 이미지)
#thresh = 임계값
#maxval = 임계값을 넘었을 때 적용할 value
#type - thresholding type
#       cv2.THRESH_BINARY
#       cv2.THRESH_BINARY_INV
#       cv2.THRESH_TRUNC
#       cv2.THRESH_TOZERO
#       cv2.THRESH_TOZERO_INVH

print('ret=', ret)
cv2.imshow('dst',  dst)

ret2, dst2 = cv2.threshold(src, 200, 255,
                             cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu의 이진화(Otsu’s Binarization)란 bimodal image에서 임계값을 자동으로 계산해주는 것
print('ret2=', ret2)
cv2.imshow('dst2',  dst2)

th3 = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
								  cv2.THRESH_BINARY, 15, 2)
#cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
#Parameters:	src - grayscale image
#				maxValue – 임계값
#				adaptiveMethod – thresholding value를 결정하는 계산 방법
#				thresholdType – threshold type
#				blockSize – thresholding을 적용할 영역 사이즈
#				C – 평균이나 가중평균에서 차감할 값
cv2.imshow('th3', th3)

cv2.waitKey()
cv2.destroyAllWindows()

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./data/0205.png',0)

ret, thresh1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)

titles =['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])

plt.show()
"""