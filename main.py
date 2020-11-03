from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys

top = 400
left = 400
width = 400
height = 300

#1 баррель нефти рублях
OIL_RUB = 3300
DOLLAR = 80
# 1 баррель нефти в долларах
OIL_DOLLAR = OIL_RUB/DOLLAR

class Converter():
    def __init__(self, ruble, dollar, oil):
        self.ruble = ruble
        self.dollar = dollar
        self.oil = oil

    def setRuble(self, ruble):
        self.ruble = ruble

    def setDollar(self, dollar):
        self.dollar = dollar

    def setOil(self, oil):
        oldOil = self.oil

    def getRuble(self):
        return str(self.ruble)

    def getDollar(self):
        return str(self.dollar)

    def getOil(self):
        return str(self.oil)

    def update(self, ruble, dollar, oil):
        oldOil = self.oil
        oldDollar = self.dollar
        oldRuble = self.ruble

        if ruble > oldRuble or ruble < oldRuble:
            self.dollar = ruble/DOLLAR
            self.oil = ruble/OIL_RUB
            self.ruble = ruble

        if dollar > oldDollar or  dollar < oldDollar:
            self.oil = dollar / OIL_DOLLAR
            self.ruble = dollar * DOLLAR
            self.dollar = dollar

        if oil > oldOil or oil < oldOil :
            self.dollar = oldDollar / (oil / oldOil)
            self.ruble = oldRuble * (oil / oldOil)
            self.oil = oil


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Генератор курса валют на торговом рынке"

        icon = "cat.jpg"

        self.converter = Converter(OIL_RUB, OIL_DOLLAR, 1)
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
        self.rubleEdit.setText(self.converter.getRuble())
        validator = QDoubleValidator(self)
        locale = QLocale("en")
        validator.setLocale(locale)
        self.rubleEdit.setValidator(validator)
        # self.rubleEdit.setReadOnly(True)

        self.dollarLabel.setText("Доллар:")
        self.dollarLabel.move(20,80)
        self.dollarLabel.setFont(QFont('Arial', 20))

        self.dollarEdit = QLineEdit(self)
        self.dollarEdit.move(150, 80)
        # self.dollarEdit.setReadOnly(True)
        self.dollarEdit.resize(200, 30)
        self.dollarEdit.setText(self.converter.getDollar())
        self.dollarEdit.setFont(QFont('Arial', 10))
        self.dollarEdit.setValidator(validator)


        self.oilLabel.setText("Нефть(баррель):")
        self.oilLabel.move(20,140)
        self.oilLabel.resize(200, 30)
        self.oilLabel.setFont(QFont('Arial', 12))

        self.oilEdit = QLineEdit(self)
        self.oilEdit.move(150, 140)
        self.oilEdit.resize(200, 30)
        self.oilEdit.setText(self.converter.getOil())
        self.oilEdit.setFont(QFont('Arial', 10))
        self.oilEdit.setValidator(validator)

        self.btn1 = QPushButton("Анализ", self)
        self.btn1.move(150,200)
        self.btn1.setFont(QFont('Arial', 10))
        self.btn1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        newRuble = float(self.rubleEdit.text())
        newDollar = float(self.dollarEdit.text())
        newOil = float(self.oilEdit.text())
        self.converter.update(newRuble, newDollar, newOil)

        self.oilEdit.setText(self.converter.getOil())
        self.rubleEdit.setText(self.converter.getRuble())
        self.dollarEdit.setText(self.converter.getDollar())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
