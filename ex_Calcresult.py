import sys
import cv2
import numpy as np
import math
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

class Calculator(QWidget):
    NumDigitButtons = 10
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.display = QLabel()

        self.digitButtons = []
        for i in range(Calculator.NumDigitButtons):
            self.digitButtons.append(self.createButton(str(i), self.digitClicked))
        #self.numberbox0 = self.createButton("0", )

        grid.setSizeConstraint(QLayout.SetFixedSize)
        grid.addWidget(self.display, 0, 0, 1, 4)
        for i in range(1, Calculator.NumDigitButtons):
            row = ((9 - i) / 3) + 2
            col = ((i - 1) % 3)
            grid.addWidget(self.digitButtons[i], row, col, 1, 1)
        grid.addWidget(self.digitButtons[0], 5, 0, 1, 2)

    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
        self.display.setText(self.display.text(), str(digitValue))

    def createButton(selfself, text, member):
        button = Button(text)
        button.clicked.connect(member)
        return button

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())