import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_layer.main_ui import Ui_MainWindow  # import the UI you generated from Qt Designer

class CoinverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect buttons to methods
        self.ui.btn_banknote_to_coin.clicked.connect(self.banknote_to_coin)
        self.ui.btn_coin_to_banknote.clicked.connect(self.coin_to_banknote)
        self.ui.btn_banknote_to_banknote.clicked.connect(self.banknote_to_banknote)

    def log(self, message):
        self.ui.log_box.append(message)

    def banknote_to_coin(self):
        self.log("[Action] Banknote-to-Coin selected.")
        # TODO: Connect to BillHandler + CoinHandler logic

    def coin_to_banknote(self):
        self.log("[Action] Coin-to-Banknote selected.")
        # TODO: Connect to CoinHandler + BillHandler logic

    def banknote_to_banknote(self):
        self.log("[Action] Banknote-to-Banknote selected.")
        # TODO: Connect to BillHandler for both input/output

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoinverterApp()
    window.show()
    sys.exit(app.exec_())
