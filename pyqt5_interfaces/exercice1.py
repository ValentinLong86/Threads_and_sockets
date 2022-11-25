import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QCoreApplication

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        grid = QGridLayout()
        widget.setLayout(grid)

        self.setCentralWidget(widget)
        self.setWindowTitle("Application Test")
        self.setFixedSize(300, 150)

        self.label = QLabel("Saisissez votre nom :") 
        self.labelNom = QLabel("")
        self.lineEdit = QLineEdit("")

        pushButton_ok = QPushButton("Ok")
        quitButton = QPushButton("Quitter")

        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.lineEdit, 1, 0)
        grid.addWidget(pushButton_ok, 2, 0)
        grid.addWidget(self.labelNom, 3, 0)
        grid.addWidget(quitButton, 4, 0)

        pushButton_ok.clicked.connect(self.actionOk)
        quitButton.clicked.connect(self.quit)

    def actionOk(self):
        self.labelNom.setText(self.lineEdit.text())

    def quit(self):
        QCoreApplication.exit(0)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    windows = MainWindows()
    windows.show()
    application.exec()
