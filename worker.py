import time

import youtube_dl
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from logger import Logger


class Worker(QObject):
    finished = pyqtSignal()
    current_progress = pyqtSignal(int)
    current_downloaded = pyqtSignal(int)
    total_size = pyqtSignal(int)

    @pyqtSlot()
    def demo(self):
        print("Python")
        for i in range(101):
            time.sleep(0.5)
            self.current_progress.emit(i)
        self.finished.emit()

    @pyqtSlot()
    def basic_downloader(self, url):
        print("Inside slot")

        def progress_hooks(d):
            print("Inside Hook")
            if d["status"] == "downloading":
                self.current_progress.emit(d['downloaded_bytes'] / d["total_bytes"] * 100)
                self.current_downloaded.emit(
                    '{}/{}'.format(d['downloaded_bytes'] / 10 ** 6, d["total_bytes"] / 10 ** 6))
            elif d["status"] == "finished":
                self.finished.emit()

        ydl_opts = {
            'logger': Logger(),
            'progress_hooks': [progress_hooks],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
