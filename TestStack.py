import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TestWin(QStackedWidget):
    def __init__(self):
        super(TestWin, self).__init__()
        #self.addWidget(QLabel("BBB"))
        self.addWidget(QPushButton("ACD"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TestWin()
    win.show()
    sys.exit(app.exec_())
