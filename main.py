from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from Dollar import Dollar
from Oil import Oil
from Ruble import Ruble

top = 400
left = 400
width = 400
height = 300

#1 баррель нефти рублях
OIL_RUB = 3300
DOLLAR = 80
# 1 баррель нефти в долларах
OIL_DOLLAR = OIL_RUB/DOLLAR

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Генератор курса валют на торговом рынке"

        icon = "cat.jpg"

        self.dollar = Dollar(OIL_DOLLAR)
        self.dollar.setDollar.connect(self.dollar.update)
        self.ruble = Ruble(OIL_RUB)
        self.ruble.setRuble.connect(self.ruble.update)
        self.oil = Oil(1)


        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setFixedSize(width, height)
        self.setWindowIcon(QIcon(icon))

        self.rubleLabel = QLabel(self)
        self.dollarLabel = QLabel(self)
        self.oilLabel = QLabel(self)

        self.rubleLabel.setText("Рубль:")
        self.rubleLabel.move(20,20)
        self.rubleLabel.setFont(QFont('Arial', 20))

        self.rubleEdit = QLineEdit(self)
        self.rubleEdit.move(150,20)
        self.rubleEdit.resize(200, 30)
        self.rubleEdit.setFont(QFont('Arial', 10))
        self.rubleEdit.setText(self.ruble.getRuble())
        validator = QDoubleValidator(self)
        locale = QLocale("en")
        validator.setLocale(locale)
        self.rubleEdit.setValidator(validator)
        self.rubleEdit.setReadOnly(True)

        self.dollarLabel.setText("Доллар:")
        self.dollarLabel.move(20,80)
        self.dollarLabel.setFont(QFont('Arial', 20))

        self.dollarEdit = QLineEdit(self)
        self.dollarEdit.move(150, 80)
        self.dollarEdit.setReadOnly(True)
        self.dollarEdit.resize(200, 30)
        self.dollarEdit.setText(self.dollar.getDollar())
        self.dollarEdit.setFont(QFont('Arial', 10))
        self.dollarEdit.setValidator(validator)

        self.oilLabel.setText("Нефть:")
        self.oilLabel.move(20,140)
        self.oilLabel.resize(200, 30)
        self.oilLabel.setFont(QFont('Arial', 20))

        self.oilEdit = QLineEdit(self)
        self.oilEdit.move(150, 140)
        self.oilEdit.resize(200, 30)
        self.oilEdit.setText(self.oil.getOil())
        self.oilEdit.setFont(QFont('Arial', 10))
        self.oilEdit.setValidator(validator)

        self.btn1 = QPushButton("Анализ", self)
        self.btn1.move(150,200)
        self.btn1.setFont(QFont('Arial', 10))
        self.btn1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        newOil = float(self.oilEdit.text())
        oldOil = float(self.oil.getOil())
        self.oil.setOil(self.oilEdit.text())
        if newOil > oldOil:
            self.ruble.setRuble.emit(1)
            self.rubleEdit.setText(self.ruble.getRuble())

            self.dollar.setDollar.emit(-1)
            self.dollarEdit.setText(self.dollar.getDollar())

        if newOil < oldOil:
            self.dollar.setDollar.emit(1)
            self.dollarEdit.setText(self.dollar.getDollar())

            self.ruble.setRuble.emit(-1)
            self.rubleEdit.setText(self.ruble.getRuble())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
