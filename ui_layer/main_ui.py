# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_banknote_to_coin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_banknote_to_coin.setGeometry(QtCore.QRect(80, 140, 121, 61))
        self.btn_banknote_to_coin.setObjectName("btn_banknote_to_coin")
        self.btn_coin_to_banknote = QtWidgets.QPushButton(self.centralwidget)
        self.btn_coin_to_banknote.setGeometry(QtCore.QRect(250, 140, 121, 61))
        self.btn_coin_to_banknote.setObjectName("btn_coin_to_banknote")
        self.btn_banknote_to_banknote = QtWidgets.QPushButton(self.centralwidget)
        self.btn_banknote_to_banknote.setGeometry(QtCore.QRect(440, 140, 121, 61))
        self.btn_banknote_to_banknote.setObjectName("btn_banknote_to_banknote")
        self.log_box = QtWidgets.QTextEdit(self.centralwidget)
        self.log_box.setGeometry(QtCore.QRect(130, 300, 331, 71))
        self.log_box.setObjectName("log_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuCoin_Converter = QtWidgets.QMenu(self.menubar)
        self.menuCoin_Converter.setObjectName("menuCoin_Converter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCoin_Converter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_banknote_to_coin.setText(_translate("MainWindow", "Banknote ➜ Coin"))
        self.btn_coin_to_banknote.setText(_translate("MainWindow", "Coin ➜ Banknote"))
        self.btn_banknote_to_banknote.setText(_translate("MainWindow", "Banknote ➜ Banknote"))
        self.menuCoin_Converter.setTitle(_translate("MainWindow", "Coin Converter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
