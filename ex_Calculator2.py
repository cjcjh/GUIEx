import math

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLayout, QLineEdit,
        QSizePolicy, QToolButton, QWidget)

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

                self.pendingAdditiveOperator = ''
                self.pendingMultiplicativeOperator = ''

                self.sumInMemory = 0.0
                self.sumSoFar = 0.0
                self.factorSoFar = 0.0
                self.waitingForOperand = True

                self.display = QLineEdit('0')   #lineedit용
                self.display.setReadOnly(True)
                self.display.setAlignment(Qt.AlignRight)
                self.display.setMaxLength(15)

                font = self.display.font()
                font.setPointSize(font.pointSize() + 8)
                self.display.setFont(font)

                self.digitButtons = []

                for i in range(Calculator.NumDigitButtons):
                        self.digitButtons.append(self.createButton(str(i), self.digitClicked))

                self.pointButton = self.createButton(".", self.pointClicked)
                self.changeSignButton = self.createButton(u"\N{PLUS-MINUS SIGN}", self.changeSignClicked)

                self.backspaceButton = self.createButton("Backspace", self.backspaceClicked)
                self.clearButton = self.createButton("Clear", self.clear)
                self.clearAllButton = self.createButton("Clear All", self.clearAll)

                self.divisionButton = self.createButton(u"\N{DIVISION SIGN}", self.multiplicativeOperatorClicked)
                self.timesButton = self.createButton(u"\N{MULTIPLICATION SIGN}", self.multiplicativeOperatorClicked)
                self.minusButton = self.createButton("-", self.additiveOperatorClicked)
                self.plusButton = self.createButton("+", self.additiveOperatorClicked)

                self.equalButton = self.createButton("=", self.equalClicked)


                mainLayout = QGridLayout()
                mainLayout.setSizeConstraint((QLayout.SetFixedSize))

                mainLayout.addWidget(self.display, 0, 0, 1, 6)
                mainLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
                mainLayout.addWidget(self.clearButton, 1, 2, 1, 2)
                mainLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)

                for i in range(1, Calculator.NumDigitButtons):          #for문 이해불가능
                        row = ((9 - i) / 3) + 2
                        column = ((i - 1) % 3) + 1
                        mainLayout.addWidget(self.digitButtons[i], row, column)

                mainLayout.addWidget(self.digitButtons[0], 5, 1)        # 0
                mainLayout.addWidget(self.pointButton, 5, 2)            # . 버튼
                mainLayout.addWidget(self.changeSignButton, 5, 3)       # +- 버튼

                mainLayout.addWidget(self.divisionButton, 2, 4)
                mainLayout.addWidget(self.timesButton, 3, 4)
                mainLayout.addWidget(self.minusButton, 4, 4)
                mainLayout.addWidget(self.plusButton, 5, 4)

                mainLayout.addWidget(self.equalButton, 5, 5)
                self.setLayout(mainLayout)

                self.setWindowTitle("Calculator")

        def digitClicked(self):
                clickedButton = self.sender()
                digitValue = int(clickedButton.text())

                if self.display.text() == '0' and digitValue == 0.0:
                        return

                if self.waitingForOperand:
                        self.display.clear()
                        self.waitingForOperand = False

                self.display.setText(self.display.text() + str(digitValue))

        def pointClicked(self):
                if self.waitingForOperand:
                        self.display.setText('0')

        def changeSignClicked(self):
                text = self.display.text()
                value = float(text)

                if value > 0.0:      # 양수이면 텍스트앞에 - 추가
                        text = "-" + text
                elif value < 0.0:       # 음수이면 첫번째 텍스트 삭제
                        text = text[1:]

                self.display.setText(text)

        def backspaceClicked(self):
                if self.waitingForOperand:
                        return

                text = self.display.text()[:-1]  # 맨마지막글자잘르기기
                if not text:
                        text = '0'
                        self.waitingForOperand = True

                self.display.setText(text)

        def clear(self):
                if self.waitingForOperand:
                        return

                self.display.setText('0')
                self.waitingForOperand = True

        def clearAll(self):
                self.sumSoFar = 0.0
                self.factorSoFar = 0.0
                self.pendingAdditiveOperator = ''
                self.pendingMultiplicativeOperator = ''
                self.display.setText('0')
                self.waitingForOperand = True

        def createButton(self, text, member):
                button = Button(text)
                button.clicked.connect(member)
                return button

        def multiplicativeOperatorClicked(self):        # x / 함수
                clickedButton = self.sender()
                clickedOperator = clickedButton.text()
                operand = float(self.display.text())

                if self.pendingMultiplicativeOperator:
                        if not self.calculate(operand, self.pendingMultiplicativeOperator):
                                self.abortOperation()
                                return

                        self.display.setText(str(self.factorSoFar))
                else:
                        self.factorSoFar = operand

                self.pendingMultiplicativeOperator = clickedOperator
                self.waitingForOperand = True

        def additiveOperatorClicked(self):
                clickedButton = self.sender()
                clickedOperator = clickedButton.text()
                operand = float(self.display.text())

                if self.pendingMultiplicativeOperator:
                        if not self.calculate(operand, self.pendingMultiplicativeOperator):
                                self.abortOperation()
                                return

                        self.display.setText(str(self.factorSoFar))
                        operand = self.factorSoFar
                        self.factorSoFar = 0.0
                        self.pendingMultiplicativeOperator = ''

                if self.pendingAdditiveOperator:
                        if not self.calculate(operand, self.pendingAdditiveOperator):
                                self.abortOperation()
                                return

                        self.display.setText(str(self.sumSoFar))
                else:
                        self.sumSoFar = operand

                self.pendingAdditiveOperator = clickedOperator
                self.waitingForOperand = True

        def abortOperation(self):
                self.clearALL()
                self.display.setText("####")

        def calculate(self, rightOperand, pendingOperator):
                if pendingOperator == "+":
                        self.sumSoFar += rightOperand
                elif pendingOperator == "-":
                        self.sumSoFar -= rightOperand
                elif pendingOperator == u"\N{MULTIPLICATION SIGN}":
                        self.factorSoFar *= rightOperand
                elif pendingOperator == u"\N{DIVISION SIGN}":
                        if rightOperand == 0.0:
                                return False

                        self.factorSoFar /= rightOperand

                return True

        def equalClicked(self):         # 정답함수수
                operand = float(self.display.text())

                if self.pendingMultiplicativeOperator:
                        if not self.calculate(operand, self.pendingMultiplicativeOperator):
                                self.abortOperation()
                                return

                        operand = self.factorSoFar
                        self.factorSoFar = 0.0
                        self.pendingMultiplicativeOperator = ''

                if self.pendingAdditiveOperator:
                        if not self.calculate(operand, self.pendingAdditiveOperator):
                                self.abortOperation()
                                return

                        self.pendingAdditiveOperator = ''
                else:
                        self.sumSoFar = operand

                self.display.setText(str(self.sumSoFar))
                self.sumSoFar = 0.0
                self.waitingForOperand = True


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())