# 0409.py
import cv2
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

##dst = src          #참조
dst = src.copy()     #복사
dst[100:400, 200:300] = 0  # 0 검은색표시

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
