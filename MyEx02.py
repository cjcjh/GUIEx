import sys
from PyQt5.QtCore import pyqtSignal, QObject
import cv2
import numpy as np
from PyQt5.QtGui import QIcon, QImage, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox, QRadioButton, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout, QToolTip
from PyQt5.QtWidgets import QAction, QFileDialog, qApp, QLabel
from PyQt5.QtGui import QFont
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Run', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(300, 50)
        btn.resize(btn.sizeHint())

        self.setLayout(grid)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('option checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Resize')
        checkbox2 = QCheckBox('rotate')
        checkbox3 = QCheckBox('hfip')
        checkbox4 = QCheckBox('vfip')
        checkbox5 = QCheckBox('rename')

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(checkbox3)
        vbox.addWidget(checkbox4)
        vbox.addWidget(checkbox5)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())