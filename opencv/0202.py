# 0202.py
import cv2

imageFile = './data/lena.jpg'   # 이미지 + 주소값 선언
img = cv2.imread(imageFile)     # cv2로 이미지 읽기, 아무옵션안되었으니 기본값 COLOR
#img= cv2.imread(imageFile, cv2.IMREAD_COLOR)
# cv2.imwrite(fileName, image) : fileName(str) = 저장될 파일명, img = 저장할 이미지
cv2.imwrite('./data/Lena.bmp', img)
cv2.imwrite('./data/Lena.png', img)
cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
# 이미지 압축률 설정, 0~9, 높을수록 압축률이 높아지고 대신 속도가 느려진다. 기본값은 3이다.
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
# jpec 압축률, 0~100
#cv2.IMWRITE_EXR_TYPE

#cv2.IMWRITE_PAM_FORMAT_GRAYSCALE

#cv2.IMWRITE_TIFF_COMPRESSION  : TIFF는 마이크로소프트에서 쓰는 방식

#cv2.IMWRITE_WEBP_QUALITY