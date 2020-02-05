import cv2

src = cv2.imread("/home/cj/Downloads/7.jpg", cv2.IMREAD_COLOR)
print(type(src))
print(src.dtype)
print(src.shape)
reresize = 1.1
dst2 = cv2.resize(src, dsize=(0, 0), fx=reresize, fy=reresize, interpolation=cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()