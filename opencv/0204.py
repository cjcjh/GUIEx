# 0204.py
import cv2
from   matplotlib import pyplot as plt


imageFile = './data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
#flag값 : cv2.IMREAD_GRAYSCALE = 0

#print(imgGray)

plt.axis('off')  # 축과 라벨을 없앤다.
# axis([xmin, xmax, ymin, ymax]) : 축의 범위를 지정한다.
# axis(‘equal’)  나중에 해보자
# axis(‘scaled’)
# axis(‘tight’)
# axis(‘image’)
# axis(‘auto’)
# axis(‘normal’)
# axis(‘square’)
# axis() 는 축과 관련된 편의 함수

plt.imshow(imgGray, cmap = "gray", interpolation='none')
plt.show()
plt.imshow(imgGray, cmap = "gray", interpolation='bicubic')
plt.show()
plt.imshow(imgGray, cmap = "gray", interpolation='nearest')
plt.show()
plt.imshow(imgGray, cmap = "binary", interpolation='bicubic')
plt.show()
plt.imshow(imgGray, cmap = "Blues", interpolation='bicubic')
plt.show()

# cmap = 'viridis', 'plasma', 'inferno', 'magma', 'cividis' 'Greys', 'Purples', 'Blues', 'Greens',
#       'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu',
#       'PuBuGn', 'BuGn', 'YlGn' 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring',
#       'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper'
# interpolation = 'none' 'bicubic' 'interp_method' 'nearest
