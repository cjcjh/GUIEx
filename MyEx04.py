import sys
from PyQt5.QtCore import pyqtSignal, QObject
import cv2
import numpy as np
from PyQt5.QtGui import QIcon, QImage, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout, QToolTip, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QAction, QFileDialog, qApp, QLabel
from PyQt5.QtGui import QFont, QPixmap
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PIL import Image


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
        grid.addWidget(self.checkbox2, 1, 0)
        grid.addWidget(self.checkbox3, 2, 0)
        grid.addWidget(self.checkbox4, 3, 0)
        grid.addWidget(self.checkbox5, 4, 0)
        grid.addWidget(QLabel('PATH'), 6, 0)
        grid.addWidget(self.lbl_img, 7, 0)

        # 2열
        self.ReSize = QLineEdit()
        self.ReSize.setAcceptDrops(False)
        grid.addWidget(self.ReSize, 0, 1)
        self.ReSize.textChanged.connect(self.image_show)
        #        self.ReSize.returnPressed.connect(self.ReSize)
        self.RoTate = QLineEdit()
        self.RoTate.setAcceptDrops(False)
        grid.addWidget(self.RoTate, 1, 1)
        self.RoTate.textChanged.connect(self.image_show)
        #        self.RoTate.returnPressed.connect(self.RoTate)

        grid.addWidget(QLabel('prefix'), 4, 1)
        self.prefix = QLineEdit()
        grid.addWidget(self.prefix, 5, 1)
        self.path = QLineEdit()
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
        reresize = self.ReSize
        rorotation = self.RoTate
        self.pixmap = search_image
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(self.pixmap)
        self.lbl_size = QLabel('Width: ' + str(self.pixmap.width()) + ', Height: ' + str(self.pixmap.height()))
        self.lbl_size.setAlignment(Qt.AlignCenter)

        #click 시 checkbox 확인인

       ##사이즈 수정
        # lbl_img.setPixmap(pixmap.scaled(640, 480, Qt.KeepAspectRatio, Qt.FastTransformation))
        # lbl_img.setPixmap(pixmap.scaledToHeight(1600, Qt.FastTransformation))
        # lbl_img.setPixmap(pixmap.scaledToWidth(1524, Qt.FastTransformation))

    #   vbox = QVBoxLayout()
    #   vbox.addWidget(lbl_img)
    #   vbox.addWidget(lbl_size)
    #   self.setLayout(vbox)

    #   self.setWindowTitle('QPixmap')
    #   self.move(300, 300)
    #   self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
