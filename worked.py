#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtGui, QtWidgets, QtPrintSupport
import DB_info


class Printer_DB(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Create some widgets
        self.setGeometry(500, 500, 300, 300)

        self.button = QtWidgets.QPushButton(
            'Print QTextEdit widget (the one below)',
            self)
        self.button.setGeometry(20, 20, 260, 30)

        self.editor = QtWidgets.QTextEdit(
            'Пожалуйста введите Номер штрих-кода',
            self)

        self.editor.setGeometry(20, 60, 260, 200)

        self.button.clicked.connect(self.print_widget)

    def print_widget(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def change_text(self):
        self.editor = QtWidgets.QTextEdit(DB_info.record, self)
        return self.editor


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Printer_DB()
    gui.show()
    app.exec_()
