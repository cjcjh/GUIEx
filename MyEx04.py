import sys
from PyQt5.QtCore import pyqtSignal, QObject
import cv2
import numpy as np
from PyQt5.QtGui import QIcon, QImage, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, \
    QGridLayout, QVBoxLayout, QToolTip, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QAction, QFileDialog, qApp, QLabel
from PyQt5.QtGui import QFont
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

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
        grid.addWidget(self.checkbox1, 0, 0)
        grid.addWidget(self.checkbox2, 1, 0)
        grid.addWidget(self.checkbox3, 2, 0)
        grid.addWidget(self.checkbox4, 3, 0)
        grid.addWidget(self.checkbox5, 4, 0)
        grid.addWidget(QLabel('PATH'), 6, 0)

        # 2열
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QLabel('prefix'), 4, 1)
        grid.addWidget(QLineEdit(), 5, 1)
        grid.addWidget(QLineEdit(), 6, 1, 1, 3)

        # 3열
        grid.addWidget(QLabel('number'), 5, 2)

        # 4열
        grid.addWidget(QPushButton('RUN'), 0, 3, 3, 1) #크기 수정해야함
        grid.addWidget(QLabel('suffix'), 4, 3)
        grid.addWidget(QLineEdit(), 5, 3)

        self.setWindowTitle('Type Here')
        self.setGeometry(300, 300, 480, 320)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
