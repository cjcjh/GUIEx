import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):   # class 만든다

   def __init__(self):
        super().__init__()  #Qwidget 상속으로 부모불러오고 나 초기화
        self.initUI()

   def initUI(self):
        self.setWindowTitle('My First Application') # 윈도우즈닉네임
        self.move(1200, 300)      # 시작좌표
        self.resize(400, 200)       # 윈도우즈크기
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)  # argv C와 같음
   ex = MyApp()
   sys.exit(app.exec_())    # return 과 같음