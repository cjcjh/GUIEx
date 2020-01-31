## Ex 5-6. QLineEdit.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    status = 'mm'

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.cb = QComboBox(self)
        self.cb.addItem('mm')
        self.cb.addItem('cm')
        self.cb.addItem('m')
        self.cb.addItem('km')
        self.cb.activated[str].connect(self.onActivated)

        self.qle = QLineEdit(self)
        self.qle.textChanged[str].connect(self.onChanged)

        grid.addWidget(self.qle, 0, 0)
        grid.addWidget(self.cb, 0, 1)

        self.label11 = QLabel('', self)
        self.label11.setAlignment(Qt.AlignCenter)
        self.label21 = QLabel('', self)
        self.label21.setAlignment(Qt.AlignCenter)
        self.label31 = QLabel('', self)
        self.label31.setAlignment(Qt.AlignCenter)
        self.label41 = QLabel('', self)
        self.label41.setAlignment(Qt.AlignCenter)

        self.label12 = QLabel('mm', self)
        self.label12.setAlignment(Qt.AlignCenter)
        self.label22 = QLabel('cm', self)
        self.label22.setAlignment(Qt.AlignCenter)
        self.label32 = QLabel('m', self)
        self.label32.setAlignment(Qt.AlignCenter)
        self.label42 = QLabel('km', self)
        self.label42.setAlignment(Qt.AlignCenter)

        grid.addWidget(self.label11, 1, 0)
        grid.addWidget(self.label12, 1, 1)
        grid.addWidget(self.label21, 2, 0)
        grid.addWidget(self.label22, 2, 1)
        grid.addWidget(self.label31, 3, 0)
        grid.addWidget(self.label32, 3, 1)
        grid.addWidget(self.label41, 4, 0)
        grid.addWidget(self.label42, 4, 1)

        self.setWindowTitle('단위환산')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeLabel(self):
        try:
            num = float(self.qle.text())

            if self.status in 'cm':
                self.label11.setText(str(num*10))
                self.label11.adjustsize()

                self.label21.setText(str(num))
                self.label21.adjustSize()

                self.label31.setText(str(num*0.01))
                self.label32.adjustSize()

                self.label41.setText(str(num*0.0001))
                self.label42.adjustSize()

            if self.status in 'mm':
                self.label11.setText(str(num))
                self.label11.adjustsize()

                self.label21.setText(str(num * 0.1))
                self.label21.adjustSize()

                self.label31.setText(str(num*0.001))
                self.label32.adjustSize()

                self.label41.setText(str(num*0.000001))
                self.label42.adjustSize()

            if self.status in 'm':
                self.label11.setText(str(num*1000))
                self.label11.adjustsize()

                self.label21.setText(str(num*100))
                self.label21.adjustSize()

                self.label31.setText(str(num*0.01))
                self.label32.adjustSize()

                self.label41.setText(str(num*0.0001))
                self.label42.adjustSize()

            if self.status in 'km':
                self.label11.setText(str(num*1000))
                self.label11.adjustsize()

                self.label21.setText(str(num))
                self.label21.adjustSize()

                self.label31.setText(str(num*0.01))
                self.label32.adjustSize()

                self.label41.setText(str(num*0.0001))
                self.label42.adjustSize()

        except ValueError :
            self.label11.setText('')
            self.label11.adjustSize()

            self.label21.setText('')
            self.label21.adjustSize()

            self.label31.setText('')
            self.label31.adjustSize()

            self.label41.setText('')
            self.label41.adjustSize()

    def onActivated(self, text):
        self.status = text
        self.changeLabel()

    def onChanged(self):
        self.changeLabel()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())