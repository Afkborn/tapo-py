
from sys import argv
from PyQt5 import QtWidgets


from python.LoginWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()
