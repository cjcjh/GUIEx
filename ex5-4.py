## Ex 5-4. QRadioButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)   ## True : 선택이 되어있게, False : 선택없이

        rbtn2 = QRadioButton(self)  ## RadioButton 중복선택 불가능 체크박스와다름
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        rbtn3 = QRadioButton(self)
        rbtn3.move(50, 90)
        rbtn3.setText('Three Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())