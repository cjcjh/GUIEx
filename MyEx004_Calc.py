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
        self.BT0 = QPushButton('0')
        self.BT1 = QPushButton('1')
        self.BT2 = QPushButton('2')
        self.BT3 = QPushButton('3')
        self.BT4 = QPushButton('4')
        self.BT5 = QPushButton('5')
        self.BT6 = QPushButton('6')
        self.BT7 = QPushButton('7')
        self.BT8 = QPushButton('8')
        self.BT9 = QPushButton('9')

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.label1, 0, 0, 1, 3)

        grid.addWidget(self.BT0, 4, 0, 3, 1)
        self.BT0.clicked.connect(self.text_change0)
        grid.addWidget(self.BT1, 3, 0)
        self.BT1.clicked.connect(self.text_change1)
        grid.addWidget(self.BT2, 3, 1)
        self.BT2.clicked.connect(self.text_change2)
        grid.addWidget(self.BT3, 3, 2)
        self.BT3.clicked.connect(self.text_change3)
        grid.addWidget(self.BT4, 2, 0)
        self.BT4.clicked.connect(self.text_change4)
        grid.addWidget(self.BT5, 2, 1)
        self.BT5.clicked.connect(self.text_change5)
        grid.addWidget(self.BT6, 2, 2)
        self.BT6.clicked.connect(self.text_change6)
        grid.addWidget(self.BT7, 1, 0)
        self.BT7.clicked.connect(self.text_change7)
        grid.addWidget(self.BT8, 1, 1)
        self.BT8.clicked.connect(self.text_change8)
        grid.addWidget(self.BT9, 1, 2)
        self.BT9.clicked.connect(self.text_change9)

        self.setWindowTitle('QGridLayout')
        self.show()

    def text_change0(self):
        ct = self.label1.text()
        self.label1.setText(ct + '0')
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
    def text_change5(self):
        ct = self.label1.text()
        self.label1.setText(ct + '5')
    def text_change6(self):
        ct = self.label1.text()
        self.label1.setText(ct + '6')
    def text_change7(self):
        ct = self.label1.text()
        self.label1.setText(ct + '7')
    def text_change8(self):
        ct = self.label1.text()
        self.label1.setText(ct + '8')
    def text_change9(self):
        ct = self.label1.text()
        self.label1.setText(ct + '9')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())