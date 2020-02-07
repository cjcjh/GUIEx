import sys
from PyQt5.QtCore import pyqtSignal, QObject
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.lb_1 = QLabel()
        self.rcn = 0

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # 사용할 위젯들 정하기
        self.Resize_BT = QPushButton('Resize')
        self.Rotate_BT = QPushButton('rotate')
        self.Hflip_BT = QPushButton('hflip')
        self.Vflip_BT = QPushButton('vflip')

        # pixmap 추가한내용
        self.pixmap = QPixmap('/home/cj/Downloads/save.png')
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap)
        self.lbl_size = QLabel('Width: ' + str(self.pixmap.width()) + ', Height: ' + str(self.pixmap.height()))
        self.lbl_size.setAlignment(Qt.AlignCenter)

        grid.addWidget(self.Resize_BT, 10, 5)
        self.Resize_BT.clicked.connect(self.image_resize)
        grid.addWidget(self.Rotate_BT, 10, 6)
        self.Rotate_BT.clicked.connect(self.image_rotation)
        grid.addWidget(self.Hflip_BT, 10, 7)
        self.Hflip_BT.clicked.connect(self.image_hflip)
        grid.addWidget(self.Vflip_BT, 10, 8)
        self.Vflip_BT.clicked.connect(self.image_vflip)
        grid.addWidget(self.lbl_img, 1, 0)

        # 2열
        self.ReSize_A = QLineEdit()
        self.ReSize_A.setAcceptDrops(False)
        grid.addWidget(self.ReSize_A, 9, 5)
        self.ReSize_A.returnPressed.connect(self.input_mask_changed)

        self.RoTate = QLineEdit()
        self.RoTate.setAcceptDrops(False)
        grid.addWidget(self.RoTate, 9, 6)
        self.RoTate.returnPressed.connect(self.input_mask_change2)

        # 4열
        self.btn = QPushButton('OPEN')
        self.btn.clicked.connect(self.open_image)
        grid.addWidget(self.btn, 10, 1)  # 크기 수정해야함

        self.setWindowTitle('Type Here')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def open_image(self):
        self.search_image = QFileDialog.getOpenFileName(self, 'Open file', '/home/', "Image files (*.jpg)")
        #self.imagePath = self.search_image[0]
        self.pixmap = QPixmap(self.search_image[0])
        self.lbl_size = QLabel('Width: ' + str(self.pixmap.width()) + ', Height: ' + str(self.pixmap.height()))
        self.lbl_size.setAlignment(Qt.AlignCenter)
        self.lbl_img.setPixmap(self.pixmap)  # 이미지 보여주는 줄
        print('open click')

# 사이즈 수정함수
    def image_resize(self):
        self.Resize_BT.clicked.connect(self.input_mask_changed)
        self.rcn += 1
        print('resize click')
        ##pixmap + cv2 활용
        if self.rcn > 1:
            img = cv2.imread(self.search_image[0])  # img = 이미지배열
            reresize = float(self.ReSize_A.text())
            self.resize_Img = cv2.resize(img, dsize=(0, 0), fx=reresize, fy=reresize, interpolation=cv2.INTER_LINEAR)
            cv2.imwrite("test.jpg", self.resize_Img)
            self.pixmap.load("test.jpg")
    def input_mask_changed(self):
        self.ReSize_A.setInputMask('0.0')

        # 이미지사이즈변경한함수컨택해야함
# 사진 각도변경
    def image_rotation(self):
        if self.Rotate_BT.isChecked() == True:
            self.input_mask_change2()
            print('rotation click')
    def input_mask_change2(self):
        self.RoTate.setInputMask('000')
        src = cv2.imread(self.pixmap, cv2.IMREAD_COLOR)
        height, width, channel = src.shape
        rorotation = float(self.RoTate.text())
        matrix = cv2.getRotationMatrix2D((width / 2, height / 2), rorotation, 1)
        self.rotation_Img = cv2.warpAffine(src, matrix, (width, height))
        self.pixmap.load(self.rotation_Img)
        # 이미지 각도변경해서출력하는함수
  # hflip 함수
    def image_hflip(self):
        print('hflip click')
        self.im = cv2.imread(self.pixmap)
        self.im2_hflip = cv2.flip(self.im, 0)
        self.pixmap.load(self.im2_hflip)
        # 이미지 뒤집는 함수
  # vflip 함수
    def image_vflip(self):
        print('vflip click')
        self.img = cv2.imread(self.search_image)
        self.im_vflip = cv2.flip(self.img, 1)
        self.pixmap.load(self.im_vflip)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())