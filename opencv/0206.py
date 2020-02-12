# 0206.py
import cv2
from   matplotlib import pyplot as plt

path = './data/'    # 경로 인식
imgBGR1 = cv2.imread(path+'lena.jpg')  # 이미지 읽기
imgBGR2 = cv2.imread(path+'apple.jpg')
imgBGR3 = cv2.imread(path+'baboon.jpg')
imgBGR4 = cv2.imread(path+'orange.jpg')

# 컬러 변환: BGR -> RGB
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

fig, ax = plt.subplots(2, 2, figsize=(5,5), sharey=True)
# fig, ax = plt.subplots(nrows = 2, ncols = 2, figsize=(10,10), sharey=True)
# matplotlib.pyplot.subplots(nrows=1, ncols=1, sharex=False,
#            sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
# 다양한 옵션들 검색할게 많다....
fig.canvas.set_window_title('Sample Pictures') # 보여줄 canvas 타이틀이름설정

ax[0][0].axis('off')
ax[0][0].imshow(imgRGB1, aspect = 'equal')
# aspect = 'auto' 'equal'

ax[0][1].axis('off')
ax[0][1].imshow(imgRGB2, aspect = 'equal')

ax[1][0].axis("off")
ax[1][0].imshow(imgRGB3, aspect = "auto")

ax[1][0].axis("off")
ax[1][1].imshow(imgRGB4, aspect = 'auto')

plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0.05, hspace=0.05)
plt.savefig("./data/0206.png", bbox_inches='tight')
# savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None 'tight', pad_inches=0.1,
#         frameon=None, metadata=None)
plt.show()
