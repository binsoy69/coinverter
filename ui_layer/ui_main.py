# ui_layer/ui_main.py
import sys
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui_layer/main_window.ui", self)

        # Connect buttons to print for now
        self.findChild(QtWidgets.QPushButton, "pushButton").clicked.connect(lambda: print("Banknote to Coin"))
        self.findChild(QtWidgets.QPushButton, "pushButton_2").clicked.connect(lambda: print("Coin to Banknote"))
        self.findChild(QtWidgets.QPushButton, "pushButton_3").clicked.connect(lambda: print("Banknote to Banknote"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
