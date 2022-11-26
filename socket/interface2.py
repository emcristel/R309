import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.lab = QLabel("température")
        self.text = QLineEdit("")
        self.temp = QLabel("")
        self.lab1 = QLabel("°C")
        self.convertir = QPushButton("Convertir")
        self.choix = QComboBox()
        self.choix.addItem("Celcius -> Kelvin")
        self.choix.addItem("Kelvin -> Celcius")
        self.lab2 = QLabel("K")
        self.button =QPushButton("?")


        grid.addWidget(self.lab, 0, 0, 1, 1)
        grid.addWidget(self.text, 0, 1, 1, 1)
        grid.addWidget(self.lab1, 0, 2, 1, 1)
        grid.addWidget(self.convertir, 2, 0, 1, 1)
        grid.addWidget(self.choix, 2, 1, 1, 1)
        grid.addWidget(self.temp, 3, 0)
        grid.addWidget(self.lab2, 3, 1, 1, 1)
        grid.addWidget(self.button,4, 2)


        self.convertir.clicked.connect(self.validation)
        self.button.clicked.connect(self.aide)
        self.choix.activated.connect(self.unite)
        self.setWindowTitle("Ma fenêtre")

    def unite(self):
        print(self.choix.currentText())
        if self.choix.currentText() == "Celcius -> Kelvin":
            self.lab1.setText("°C")
            self.lab2.setText("K")
        else:
            self.lab1.setText("K")
            self.lab2.setText("°C")

    def validation(self):
        try:
            degres = self.text.text()
            if self.choix.currentText() == "Celcius -> Kelvin":
                kelvin = float(degres) + 273.15
                self.temp.setText(f"{kelvin}")
            else:
                kelvin = float(degres) - 273.15
                self.temp.setText(f"{kelvin}")
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Entrez un nombre")


    def aide(self):
        QMessageBox.information(self, "Aide", "Entrez un nombre de degrés et cliquez sur convertir en Clesius ou en Kelvin")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()