import sys
import os
import cv2
import re
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

mod = sys.modules[__name__]

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("Image Augmentation")
        self.setFixedWidth(640)
        self.setFixedHeight(480)

        self.check_list = ["Resize", "Rotate", "hFlip", "vFlip", "rename"]

        self.size = QLineEdit(self)
        self.rotate = QLineEdit(self)

        self.run = QPushButton('Run', self)

        self.prefix_label = QLabel('prefix', self)
        self.suffix_label = QLabel('suffix', self)
        self.number_label = QLabel('number', self)
        self.prefix = QLineEdit(self)
        self.suffix = QLineEdit(self)

        self.path_label = QLabel('PATH', self)
        self.path = QLineEdit(self)

        for CB in self.check_list:
            setattr(mod, f'CH_{CB}', QCheckBox(CB, self))

        self.layout_base = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.init_widget()

    def init_widget(self):
        self.size.move(180, 60)
        self.size.resize(150, 30)
        self.rotate.move(180, 140)
        self.rotate.resize(150, 30)

        self.run.move(410, 30)
        self.run.resize(150, 110)
        self.run.clicked.connect(self.augment)

        self.prefix_label.move(320, 360)
        self.suffix_label.move(520, 360)
        self.prefix.move(300, 390)
        self.suffix.move(500, 390)
        self.number_label.move(410, 390)

        self.path_label.move(180, 430)
        self.path.move(280, 430)
        self.path.resize(330, 30)

        for CB in self.check_list:
            self.layout_base.addWidget(eval(f'CH_{CB}'))
####################################################################
    def augment(self):
        print('[#] Run button clicked')
        img = cv2.imread(self.path.text())
        path = self.path.text()
        for i in self.check_list:
            if eval(f'CH_{i}').isChecked() == True:
                if i == 'rename':
                    path = self.image_rename()
                else:
                    print('[#] function call::' + f'image_{i}')
                    img = eval(f'self.image_{i}(img)')
        cv2.imwrite(path, img)
####################################################################
    def image_Resize(self, img):
        width, height, _ = img.shape
        matched_text = re.findall(r'\d+', self.size.text())
        if len(matched_text) == 0:
            print('[!] not enough size parameters')
        width = matched_text[0]
        if len(matched_text) > 1:
             height = matched_text[1]

        return cv2.resize(img, (int(height), int(width)))

    def image_Rotate(self, img):
        if self.rotate.text() == None:
            msg = QMessageBox()
        (h, w) = img.shape[:2]
        (cX, cY) = (w // 2, h // 2)

        M = cv2.getRotationMatrix2D((cX, cY), -int(self.rotate.text()), 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])

        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))

        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY

        return cv2.warpAffine(img, M, (nW, nH))

    def image_hFlip(self, img):
        return cv2.flip(img, 1)

    def image_vFlip(self, img):
        return cv2.flip(img, 0)

    def image_rename(self):
        dir, file = os.path.split(self.path.text())
        prefix = self.prefix.text()
        suffix = self.suffix.text()
        if prefix:
            file = prefix + file
        if suffix:
            file, ext = os.path.splitext(file)
            file = file + suffix + ext

        return os.path.join(dir, file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())