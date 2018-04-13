#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600, 500)
    w.move(300, 300)
    w.setWindowTitle("Mooi!")

    b = QPushButton(w)

    w.show()
    
    sys.exit(app.exec_())