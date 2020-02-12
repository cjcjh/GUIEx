# 0201.py
import cv2

imageFile = './data/lena.jpg'    # 이미지경로지정
# cv2.imread(fileName, flag) : filename(str) - 이미지파일의경로, flag(int) : 읽을 때 옵션
img  = cv2.imread(imageFile, cv2.IMREAD_COLOR)    # cv2.IMREAD_COLOR : 기본값임
img2 = cv2.imread(imageFile, 0) # 0 = cv2.IMREAD_GRAYSCALE,

print("IMREAD_GRAYSCALE:" + str(cv2.IMREAD_GRAYSCALE))  # imread, 옵션 0
print("IMREAD_COLOR:" + str(cv2.IMREAD_COLOR))          # imread, 옵션 1
print("IMREAD_UNCHANGED:" + str(cv2.IMREAD_UNCHANGED))  # imread, 옵션 -1

cv2.imshow('Lena color',img)
cv2.imshow('Lena grayscale',img2)

cv2.waitKey()
cv2.destroyAllWindows()