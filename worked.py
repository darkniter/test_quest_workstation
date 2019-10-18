
import sys

from PyQt5 import QtGui, QtPrintSupport
from PyQt5.QtWidgets import QApplication, QWidget
import config
import tempfile
import json


def get_records():
    with open(config.DATA, 'r+', encoding='utf-8') as data_file:
        data_obj = json.load(data_file)
    return data_obj


def print_from_printer():
    return(QtPrintSupport.QPrinterInfo.defaultPrinterName())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle(print_from_printer())
    w.show()

    sys.exit(app.exec_())
