import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtCore import QCoreApplication


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        grid = QGridLayout()
        widget.setLayout(grid)

        self.setCentralWidget(widget)
        self.setWindowTitle("Application Test")

        self.label = QLabel("Température") 
        self.label2 = QLabel("Conversion")
        self.Klabel = QLabel("K") 
        self.Clabel2 = QLabel("°C")
        self.lineEdit = QLineEdit("")
        self.conversionfield = QLineEdit("")
        self.conversionfield.setEnabled(False)

        self.comboxBox = QComboBox()
        self.comboxBox.addItem("°C -> K")
        self.comboxBox.addItem("K -> °C")

        self.comboxBox.currentIndexChanged.connect(self.calcul)

        pushButton_Convertir = QPushButton("Convertir")
        pushButton_Convertir.clicked.connect(self.calcul2)
        helpButton = QPushButton("AIDEZ MOI")
        helpButton.clicked.connect(self.help)

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.lineEdit, 0, 1)
        grid.addWidget(self.Clabel2, 0, 2)
       
        grid.addWidget(self.Clabel2, 0, 2)
        grid.addWidget(pushButton_Convertir, 1, 1)
        grid.addWidget(self.comboxBox, 1, 2)

        grid.addWidget(self.label2, 2, 0)
        grid.addWidget(self.conversionfield, 2, 1)
        grid.addWidget(self.Klabel, 2, 2)

        grid.addWidget(helpButton, 3, 3)

    def calcul(self):
        if self.comboxBox.currentIndex() == 0:
            self.Klabel.setText("K")
            self.Clabel2.setText("°C")
            
        elif self.comboxBox.currentIndex() == 1:
            self.Klabel.setText("°C")
            self.Clabel2.setText("K")

    def calcul2(self):
        try:
            float(self.lineEdit.text())
        except:
            self.conversionfield.setText("Un nombre SVP")
            return 0

        if self.comboxBox.currentIndex() == 0:
            calcul = str((float(self.lineEdit.text())) + 273.15)
            if float(self.lineEdit.text()) < -273.15:
                self.conversionfield.setText("C'est impossible")
                return 0
        elif self.comboxBox.currentIndex() == 1:
            calcul = str((float(self.lineEdit.text())) - 273.15)
            if float(self.lineEdit.text()) < 0:
                self.conversionfield.setText("C'est impossible")
                return 0
        
        self.conversionfield.setText(calcul)

    def help(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Permet de convertir un nombre soit de Kelvin vers Celcius, soit de Celsius vers Kelvin")
        self.msgBox.setWindowTitle("Aide")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.show()


if __name__ == "__main__":
    application = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    application.exec()
