## Ex 5-1. QPushButton.
## 추가문제 버튼1클릭시 버튼3 표시변환되게하
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('&Button1', self)
        self.btn1.setCheckable(True)
        self.btn1.toggle()

        self.btn2 = QPushButton(self)
        self.btn2.setText('Button&2')

        self.btn3 = QPushButton('Button3', self)
        self.btn3.setEnabled(False)

        self.btn3.clicked.connect(self.changeEnable)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeEnable(self):
        self.btn3.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())