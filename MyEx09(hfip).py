import sys
from PyQt5.QtCore import pyqtSignal, QObject
import cv2
import numpy as np
from PyQt5.QtGui import QIcon, QImage, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout, QToolTip, QTextEdit
from PyQt5.QtWidgets import QAction, QFileDialog, qApp, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PIL import Image

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.lb_1 = QLabel()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # option 정하기
        # 1열
        self.checkbox1 = QCheckBox('Resize')
        self.checkbox2 = QCheckBox('rotate')
        self.checkbox3 = QCheckBox('hfip')
        self.checkbox4 = QCheckBox('vfip')
        self.checkbox5 = QCheckBox('rename')

        # pixmap 추가한내용
        self.pixmap = QPixmap('/home/cj/Downloads/save.png')
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap)
        self.lbl_size = QLabel('Width: ' + str(self.pixmap.width()) + ', Height: ' + str(self.pixmap.height()))
        self.lbl_size.setAlignment(Qt.AlignCenter)

        grid.addWidget(self.checkbox1, 0, 0)
        self.checkbox1.stateChanged.connect(self.image_resize)
        grid.addWidget(self.checkbox2, 1, 0)
        self.checkbox2.stateChanged.connect(self.image_rotation)
        grid.addWidget(self.checkbox3, 2, 0)
        self.checkbox3.stateChanged.connect(self.image_hflip)
        grid.addWidget(self.checkbox4, 3, 0)
        self.checkbox4.stateChanged.connect(self.image_vflip)
        grid.addWidget(self.checkbox5, 4, 0)
        self.checkbox5.stateChanged.connect(self.image_show)
        grid.addWidget(QLabel('PATH'), 6, 0)
        grid.addWidget(self.lbl_img, 7, 0)

        # 2열
        self.ReSize_A = QLineEdit()
        self.ReSize_A.setAcceptDrops(False)
        grid.addWidget(self.ReSize_A, 0, 1)
        self.ReSize_A.returnPressed.connect(self.input_mask_changed)

        self.RoTate = QLineEdit()
        self.RoTate.setAcceptDrops(False)
        grid.addWidget(self.RoTate, 1, 1)
        self.RoTate.returnPressed.connect(self.input_mask_change2)

        grid.addWidget(QLabel('prefix'), 4, 1)
        self.prefix = QLineEdit()
        self.prefix.setAcceptDrops(False)
        grid.addWidget(self.prefix, 5, 1)
        self.prefix.returnPressed.connect(self.image_show)

        self.path = QLineEdit()
        self.path.setAcceptDrops(False)
        grid.addWidget(self.path, 6, 1, 1, 3)
        self.path.returnPressed.connect(self.image_show)

        # 3열
        grid.addWidget(QLabel('number'), 5, 2)

        # 4열
        self.btn = QPushButton('RUN')
        self.btn.clicked.connect(self.image_show)
        grid.addWidget(self.btn, 0, 3, 3, 1)  # 크기 수정해야함
        grid.addWidget(QLabel('suffix'), 4, 3)
        self.suffix = QLineEdit()
        grid.addWidget(self.suffix, 5, 3)

        self.setWindowTitle('Type Here')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def image_show(self):
        search_image = '/home/cj/Downloads/' + self.path.text()
        self.pixmap = QPixmap(search_image)
        self.lbl_size = QLabel('Width: ' + str(self.pixmap.width()) + ', Height: ' + str(self.pixmap.height()))
        self.lbl_size.setAlignment(Qt.AlignCenter)

        #click 시 checkbox 확인인
        #사이즈 수정
        if self.checkbox1.isChecked() == True:
            ##pixmap + cv2 활용
            img = cv2.imread(search_image)
            reresize = float(self.ReSize_A.text())
            resize_Img = cv2.resize(img, dsize=(0, 0), fx=reresize, fy=reresize, interpolation=cv2.INTER_LINEAR)
            cv2.imwrite("test.jpg", resize_Img)
            self.pixmap.load("test.jpg")

        # 각도회전
        if self.checkbox2.isChecked() == True:
            src = cv2.imread(search_image, cv2.IMREAD_COLOR)
            height, width, channel = src.shape
            rorotation = float(self.RoTate.text())
            matrix = cv2.getRotationMatrix2D((width/2, height/2), rorotation, 1)
            rotation_Img = cv2.warpAffine(src, matrix, (width, height))
            cv2.imwrite("rotation.jpg", rotation_Img)
            self.pixmap.load("rotation.jpg")

        if self.checkbox3.isChecked() == True:
            im = cv2.imread(search_image)
            im2 = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            im2_hflip = cv2.flip(im, 0)
            cv2.imwrite("im_hflip.jpg", im2_hflip)
            self.pixmap.load("im_hflip.jpg")

        self.lbl_img.setPixmap(self.pixmap)  # 이미지 보여주는 줄
        print('이미지 출력완료')


  # 사이즈 수정함수
    def image_resize(self):
        if self.checkbox1.isChecked() == True:
            self.input_mask_changed()
    def input_mask_changed(self):
        self.ReSize_A.setInputMask('0.0')
  # 사진 각도변경
    def image_rotation(self):
        if self.checkbox2.isChecked() == True:
            self.input_mask_change2()
    def input_mask_change2(self):
        self.RoTate.setInputMask('000')
  # hflip 함수
    def image_hflip(self):
        #if self.checkbox3.isChecked() == True:
        print('click')
        #elif self.checkbox3.isChecked() == False:



  # vflip 함수
    def image_vflip(self):
    #    if self.check
        print('click2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())