# 0503.py
import cv2
import numpy as np

src = np.array([[0, 0, 0, 0],
              [1, 1, 3, 5],
              [6, 1, 1, 3],
              [4, 3, 1, 7]
              ], dtype=np.uint8)

hist1 = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[4], ranges=[0, 8])
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
# Parameters:
# image – 분석대상 이미지(uint8 or float32 type). Array형태.
# channels – 분석 채널(X축의 대상). 이미지가 graysacle이면 [0], color 이미지이면 [0],[0,1] 형태(1 : Blue, 2: Green, 3: Red)
# mask – 이미지의 분석영역. None이면 전체 영역.
# histSize – BINS 값. [256]
# ranges – Range값. [0,256]
print('hist1 = ', hist1)

hist2 = cv2.calcHist(images=[src], channels=[0], mask=None,
                    histSize=[4], ranges=[0, 4])
print('hist2 = ', hist2)
