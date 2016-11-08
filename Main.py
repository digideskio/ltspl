from PyQt5.QtWidgets import *
from PyQt5 import Qt


class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setWindowTitle("Hello World")
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.pre_pos = None

    def mousePressEvent(self, event):
        self.pre_pos = self.pos() - event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(event.globalPos() + self.pre_pos)

    def mouseReleaseEvent(self, event):
        pass

    def setLayout(self, layout):
        super.setlayout(layout)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
