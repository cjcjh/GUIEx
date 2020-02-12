# 0205.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.figure(figsize=(6,6))
# fig=figure(num=figure number, figsize=(x,y)) : figsize 인치단위로입력
# fig=figure(figure number, (x,y))
# fig=figure()
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
# subplots_adjust 서브플롯 간 간격 조절하기 left, bottom, right, top, wspace, hspace 의 간격을 조절할 수 있음
plt.imshow(imgGray, cmap = 'gray')
plt.show()
plt.subplots_adjust(left=0, right=0.5, bottom=0, top=1)
plt.imshow(imgGray, cmap = 'gray')
plt.show()
plt.subplots_adjust(left=0, right=3, bottom=0, top=3)
plt.imshow(imgGray, cmap = 'gray')
plt.show()
##plt.axis('tight')
plt.axis('off')
plt.savefig('./data/0205.png')
# plt.show()
