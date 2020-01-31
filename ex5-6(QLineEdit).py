## Ex 5-6. QLineEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)     ## 레이블 : 출력하는거 o
        self.lbl.move(60, 50)      ## 적은 글자 표시

        qle = QLineEdit(self)       ## 적은 글자 쓸공간
        qle.move(60, 10)
        qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()   ## 몇글자입력하느냐에 따라 맞춰서 사이즈 변

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())