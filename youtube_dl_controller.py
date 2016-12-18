import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread

from worker import Worker


class UIContoller(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('youtube_dl.ui',self)
        self.pushButton.clicked.connect(self.on_button_pressed_handle)
        self.show()

    def on_button_pressed_handle(self):
        self.worker = Worker()
        self.thread = QThread()
        print("HI")
        self.worker.current_progress.connect(self.progressbar_updater)

        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(sys.exit)

        self.thread.started.connect(lambda: self.worker.basic_downloader(self.lineEdit.text()))
        self.thread.start()

    def progressbar_updater(self, progress):
        self.progressBar.setValue(progress)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = UIContoller()
    sys.exit(app.exec_())
