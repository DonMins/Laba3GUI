import sys
from PyQt5.QtCore import pyqtSignal, QObject


class Ruble(QObject):
    setRuble = pyqtSignal(int)

    def __init__(self, ruble):
        super().__init__()
        self.ruble = ruble

    def update(self, value):
        if value > 0:
            self.ruble = self.ruble * 2
        else:
            self.ruble = self.ruble / 2

    def getRuble(self):
        return str(self.ruble)
