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
        #    QToolTip.setFont(QFont('SansSerif', 10))
        #    self.setToolTip('This is a <b>QWidget</b> widget')

        # option 정하기
        # 1열
        self.checkbox1 = QCheckBox('Resize')
        self.checkbox2 = QCheckBox('rotate')
        self.checkbox3 = QCheckBox('hfip')
        self.checkbox4 = QCheckBox('vfip')
        self.checkbox5 = QCheckBox('rename')

        # pixmap 추가한내용
        #im = Image.fromarray(np.random.randint(0, 256, size=(100, 100, 3)).astype(np.uint8))
        self.pixmap = QPixmap('/home/cj/Downloads/save.png')
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap)
        self.lbl_size = QLabel('Width: ' + str(self.pixmap.width()) + ', Height: ' + str(self.pixmap.height()))
        self.lbl_size.setAlignment(Qt.AlignCenter)

        grid.addWidget(self.checkbox1, 0, 0)
        self.checkbox1.stateChanged.connect(self.image_resize)
        grid.addWidget(self.checkbox2, 1, 0)
        self.checkbox2.stateChanged.connect(self.image_show)
        grid.addWidget(self.checkbox3, 2, 0)
        self.checkbox3.stateChanged.connect(self.image_show)
        grid.addWidget(self.checkbox4, 3, 0)
        self.checkbox4.stateChanged.connect(self.image_show)
        grid.addWidget(self.checkbox5, 4, 0)
        self.checkbox5.stateChanged.connect(self.image_show)
        grid.addWidget(QLabel('PATH'), 6, 0)
        grid.addWidget(self.lbl_img, 7, 0)

        # 2열
        self.ReSize_A = QLineEdit()
        self.ReSize_A.setAcceptDrops(False)
        #self.ReSize_A.setInputMask(0.0)
        #self.ReSize_A.setPlaceholderText('Float Number')
        #self.ReSize_A.act.connect(self.input_mask_changed)
        grid.addWidget(self.ReSize_A, 0, 1)
        self.ReSize_A.returnPressed.connect(self.input_mask_changed)

        self.RoTate = QLineEdit()
        self.RoTate.setAcceptDrops(False)
        grid.addWidget(self.RoTate, 1, 1)
        self.RoTate.returnPressed.connect(self.image_show)

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

        ##사이즈 수정
        # lbl_img.setPixmap(pixmap.scaled(640, 480, Qt.KeepAspectRatio, Qt.FastTransformation))
        # lbl_img.setPixmap(pixmap.scaledToHeight(1600, Qt.FastTransformation))
        # lbl_img.setPixmap(pixmap.scaledToWidth(1524, Qt.FastTransformation))

        #click 시 checkbox 확인인
        #사이즈 수정
        if self.checkbox1.isChecked() == True:
##pixmap
            img = cv2.imread(search_image)
            reresize = float(self.ReSize_A.text())
            self.dst = cv2.resize(img, dsize=(0, 0), fx=reresize, fy=reresize, interpolation=cv2.INTER_LINEAR)
            cv2.imshow('dst', self.dst)
#            t_width = int(self.pixmap.width())*float(self.ReSize_A.text())
#            temp = self.ReSize_A.text()
#            t_height = int(self.pixmap.height())*float(self.ReSize_A.text())
 #           print(t_width)
 #           print(t_height)

            #self.lbl_size.set('Width: ' + str(t_width) + ', Height: ' + str(t_height))
            #self.lbl_size.setAlignment(Qt.AlignCenter)
            #self.lbl_img.setPixmap(self.pixmap.scaled(self.pixmap.width()*self.ReSize_A, self.pixmap.height()*self.ReSize_A, Qt.KeepAspectRatio, Qt.FastTransformation))


        self.lbl_img.setPixmap(self.pixmap)  # 이미지 보여주는 줄
        print('이미지 출력완료')

        # 각도회전
        rorotation = self.RoTate

        # 사이즈 수정함수
    def image_resize(self):
        if self.checkbox1.isChecked() == True:
            self.input_mask_changed()
    def input_mask_changed(self):
        self.ReSize_A.setInputMask('0.0')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
