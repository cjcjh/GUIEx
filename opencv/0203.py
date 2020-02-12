# 0203.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'   # 이미지경로선언
imgBGR = cv2.imread(imageFile) # cv2.IMREAD_COLOR
# cv2.imread(filename, flags)
# print(type(imgBGR))
# plt.imshow(imgBGR)
# plt.show()
# plt.axis('off')
# plt.imshow(imgBGR)
# plt.show()

imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
# cv2.cvtColor( image, 변환 코드 )
# BGR -> Grayscale : cv2.COLOR_BGR2GRAY
# BGR -> HSV : cv2.COLOR_BGR2HSV
#imgRGB = cv2.cvtColor(imageFile, cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.show()
