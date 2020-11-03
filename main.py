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
f = open('text.txt', 'w')

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Генератор курса валют на торговом рынке"

        icon = "cat.jpg"

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
        self.rubleEdit.setValidator(QDoubleValidator())
        self.rubleEdit.setReadOnly(True)

        self.dollarLabel.setText("Доллар:")
        self.dollarLabel.move(20,80)
        self.dollarLabel.setFont(QFont('Arial', 20))

        self.dollarEdit = QLineEdit(self)
        self.dollarEdit.move(150, 80)
        self.dollarEdit.setReadOnly(True)
        self.dollarEdit.resize(200, 30)
        self.dollarEdit.setFont(QFont('Arial', 10))
        self.dollarEdit.setValidator(QDoubleValidator())

        self.oilLabel.setText("Нефть($):")
        self.oilLabel.move(20,140)
        self.oilLabel.resize(200, 30)
        self.oilLabel.setFont(QFont('Arial', 20))

        self.oilEdit = QLineEdit(self)
        self.oilEdit.move(150, 140)
        self.oilEdit.resize(200, 30)
        self.oilEdit.setFont(QFont('Arial', 10))
        self.oilEdit.setValidator(QDoubleValidator())

        self.btn1 = QPushButton("Анализ", self)
        self.btn1.move(150,200)
        self.btn1.setFont(QFont('Arial', 10))
        self.btn1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
