import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import *
from PyQt5 import QtCore

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 300, 200)
        self.label1 = QLabel('')
        self.label1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        #self.label1.setFixedWidth(350)
        self.BT1 = QPushButton('1')
        self.BT2 = QPushButton('2')
        self.BT3 = QPushButton('3')
        self.Bt4 = QPushButton('4')

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.label1, 0, 0, 1, 0)

        grid.addWidget(self.BT1, 1, 0)
        self.BT1.clicked.connect(self.text_change1)
        grid.addWidget(self.BT2, 1, 1)
        self.BT2.clicked.connect(self.text_change2)
        grid.addWidget(self.BT3, 2, 0)
        self.BT3.clicked.connect(self.text_change3)
        grid.addWidget(self.Bt4, 2, 1)
        self.Bt4.clicked.connect(self.text_change4)

        self.setWindowTitle('QGridLayout')
        self.show()

    def text_change1(self):
        ct = self.label1.text()
        self.label1.setText(ct + '1')
    def text_change2(self):
        ct = self.label1.text()
        self.label1.setText(ct + '2')
    def text_change3(self):
        ct = self.label1.text()
        self.label1.setText(ct + '3')
    def text_change4(self):
        ct = self.label1.text()
        self.label1.setText(ct + '4')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())