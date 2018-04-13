#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600, 500)
    w.move(300, 300)
    w.setWindowTitle("Mooi!")

    my_label = QLabel("Hieronder staat een knop")

    b = QPushButton(w)
    b.setText("Druk op mij")

    my_layout = QVBoxLayout(w)
    my_layout.addWidget(my_label)
    my_layout.addWidget(b)

    w.show()
    
    sys.exit(app.exec_())