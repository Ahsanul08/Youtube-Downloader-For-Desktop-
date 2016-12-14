from PyQt5 import QtWidgets, uic
import sys


class UIContoller(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('youtube_dl.ui',self)
        self.pushButton.clicked.connect(self.on_button_pressed_handle)
        self.show()

    def on_button_pressed_handle(self):
        self.label.setText(self.lineEdit.text())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = UIContoller()
    sys.exit(app.exec_())
