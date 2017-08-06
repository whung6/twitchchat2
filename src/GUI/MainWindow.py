import sys
import ctypes
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QPoint
from CentralWidget import CentralWidget
from MenuBar import MenuBar
from CacheManager import CacheManager
import os.path

class MainWindow(QMainWindow):
    def __init__(self):
        if not os.path.exists(CacheManager.DIRECTORY):
            os.mkdir(CacheManager.DIRECTORY)
        user32 = ctypes.windll.user32
        super().__init__()
        self.setWindowTitle('Twitch chat')
        self.left = user32.GetSystemMetrics(0) - 900
        self.top = 40
        self.width = 500
        self.height = user32.GetSystemMetrics(1) - 100
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.centralWidget = CentralWidget(self)
        self.setCentralWidget(self.centralWidget)

        menu = MenuBar(self)
        self.setMenuBar(menu)

        self.show()

    def getPopUpPosition(self, x, y):
        pos = self.mapToGlobal(QPoint(self.width/2, self.height/2))
        pos -= QPoint(x / 2, y / 2)
        return pos

    def closeEvent(self, event):
        CacheManager.clearCache()
        #leave all channel
        #clear cache
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
