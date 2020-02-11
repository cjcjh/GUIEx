import sys
from functools import partial
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout,
                        QLayout, QSizePolicy, QToolButton, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSlot

"""
class Button(QToolButton):
    def __init__(self, text, parent=None):
        super(Button, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size
"""
class MyApp(QWidget):

    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.initUI()

    def initUI(self):
        self.result_text1 = ''
        self.result_text2 = ''
        self.result_text3 = ''
        self.label1 = QLabel('')
        self.label1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.BT0 = QPushButton('0')
        self.BT1 = QPushButton('1')
        self.BT2 = QPushButton('2')
        self.BT3 = QPushButton('3')
        self.BTEnter = QPushButton('Enter')
        self.BT4 = QPushButton('4')
        self.BT5 = QPushButton('5')
        self.BT6 = QPushButton('6')
        self.BT7 = QPushButton('7')
        self.BT8 = QPushButton('8')
        self.BT9 = QPushButton('9')
        self.BTPlus = QPushButton('+')
        self.BTDivid = QPushButton('/')
        self.BTMultiply = QPushButton('*')
        self.BTMinus = QPushButton('-')

        self.setFixedSize(200, 250)
        self.generalLayout = QVBoxLayout()
        grid = QGridLayout()
        grid.setRowStretch(1, 4)
        grid.setRowStretch(2, 4)
        grid.setRowStretch(3, 4)
        grid.setRowStretch(4, 4)
        grid.setRowStretch(5, 4)
        grid.setRowStretch(6, 4)
        self.setLayout(grid)

        grid.addWidget(self.label1, 0, 0, 1, 4)


        grid.addWidget(self.BT0, 5, 0, 1, 2)
        self.BT0.setFixedSize(80+3, 40)
        print(grid.verticalSpacing())     # 그래드 이미지 사이 공간
        print(grid.horizontalSpacing())
        self.BT0.clicked.connect(self.text_change0)
        grid.addWidget(self.BT1, 4, 0, 1, 1)
        self.BT1.setFixedSize(40, 40)
        self.BT1.clicked.connect(self.text_change1)
        grid.addWidget(self.BT2, 4, 1, 1, 1)
        self.BT2.setFixedSize(40, 40)
        self.BT2.clicked.connect(self.text_change2)
        grid.addWidget(self.BT3, 4, 2, 1, 1)
        self.BT3.setFixedSize(40, 40)
        self.BT3.clicked.connect(self.text_change3)
        grid.addWidget(self.BTEnter, 4, 3, 2, 1)
        self.BTEnter.setFixedHeight(80+3)
        self.BTEnter.clicked.connect(self.text_result)

        grid.addWidget(self.BT4, 3, 0, 1, 1)
        self.BT4.setFixedSize(40, 40)
        self.BT4.clicked.connect(self.text_change4)
        grid.addWidget(self.BT5, 3, 1, 1, 1)
        self.BT5.setFixedSize(40, 40)
        self.BT5.clicked.connect(self.text_change5)
        grid.addWidget(self.BT6, 3, 2, 1, 1)
        self.BT6.setFixedSize(40, 40)
        self.BT6.clicked.connect(self.text_change6)

        grid.addWidget(self.BT7, 2, 0, 1, 1)
        self.BT7.setFixedSize(40, 40)
        self.BT7.clicked.connect(self.text_change7)
        grid.addWidget(self.BT8, 2, 1, 1, 1)
        self.BT8.setFixedSize(40, 40)
        self.BT8.clicked.connect(self.text_change8)
        grid.addWidget(self.BT9, 2, 2, 1, 1)
        self.BT9.setFixedSize(40, 40)
        self.BT9.clicked.connect(self.text_change9)
        grid.addWidget(self.BTPlus, 2, 3, 2, 1)
        self.BTPlus.setFixedHeight(80+3)
        self.BTPlus.clicked.connect(self.text_Plus)

        grid.addWidget(self.BTDivid, 1, 1, 1, 1)
        self.BTDivid.setFixedSize(40, 40)
        self.BTDivid.clicked.connect(self.text_Divid)
        grid.addWidget(self.BTMultiply, 1, 2, 1, 1)
        self.BTMultiply.setFixedSize(40, 40)
        self.BTMultiply.clicked.connect(self.text_Multiply)
        grid.addWidget(self.BTMinus, 1, 3, 1, 1)
        self.BTMinus.setFixedSize(40, 40)
        self.BTMinus.clicked.connect(self.text_Minus)

        self.setWindowTitle('QGridLayout')
        self.show()

    def text_change0(self):
        ct = self.label1.text()
        self.label1.setText(ct + '0')
        self.result_text1 = float(self.label1.text())
        print(self.result_text1)
    def text_change1(self):
        ct = self.label1.text()
        self.label1.setText(ct + '1')
        self.result_text1 = float(self.label1.text())
    def text_change2(self):
        ct = self.label1.text()
        self.label1.setText(ct + '2')
        self.result_text1 = float(self.label1.text())
    def text_change3(self):
        ct = self.label1.text()
        self.label1.setText(ct + '3')
        self.result_text1 = float(self.label1.text())
    def text_change4(self):
        ct = self.label1.text()
        self.label1.setText(ct + '4')
        self.result_text1 = float(self.label1.text())
    def text_change5(self):
        ct = self.label1.text()
        self.label1.setText(ct + '5')
        self.result_text1 = float(self.label1.text())
    def text_change6(self):
        ct = self.label1.text()
        self.label1.setText(ct + '6')
        self.result_text1 = float(self.label1.text())
    def text_change7(self):
        ct = self.label1.text()
        self.label1.setText(ct + '7')
        self.result_text1 = float(self.label1.text())
    def text_change8(self):
        ct = self.label1.text()
        self.label1.setText(ct + '8')
        self.result_text1 = float(self.label1.text())
    def text_change9(self):
        ct = self.label1.text()
        self.label1.setText(ct + '9')
        self.result_text1 = float(self.label1.text())

    def text_Plus(self):
        self.result_text2 = '+'
        self.result_text3 = float(self.label1.text())
        self.label1.setText("")
    def text_Divid(self):
        self.result_text2 = '/'
        self.result_text3 = float(self.label1.text())
        self.label1.setText("")
    def text_Multiply(self):
        self.result_text2 = '*'
        self.result_text3 = float(self.label1.text())
        self.label1.setText("")
    def text_Minus(self):
        self.result_text2 = '-'
        self.result_text3 = float(self.label1.text())
        self.label1.setText("")

    def text_result(self):
        self.result_text1 = self.label1.text()
        if self.result_text2 == "+":
            self.result_text3 += float(self.result_text1)
        elif self.result_text2 == "-":
            self.result_text3 -= float(self.result_text1)
        elif self.result_text2 == "*":
            self.result_text3 *= float(self.result_text1)
        elif self.result_text2 == "/":
            self.result_text3 /= float(self.result_text1)
        self.label1.setText(str(self.result_text3))
"""
    def createButton(self, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())