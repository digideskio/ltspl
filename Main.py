from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from LoginViewUI import LoginView
from StatusViewUI import StatusView
import UICreatetor
import RestrictedAssetChecker

def exit_app():
    QApplication.exit()


class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        self.login_view = LoginView()
        self.status_view = StatusView()
        self.shadow = QLabel()
        self.setup_ui()

    def onAddToScreen(self):
        self.login_view.easing_in()
        #self.status_view.easing_in()
        self.shadow.setVisible(True)
        m = MainThread()
        m.begin_play(self)

    def show(self):
        super(MainWin, self).show()
        self.onAddToScreen()

    def mousePressEvent(self, event):
        self.pre_pos = self.pos() - event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(event.globalPos() + self.pre_pos)

    def mouseReleaseEvent(self, event):
        pass

    def setup_ui(self):
        self.setWindowTitle("Hello World")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(480, 400)
        stack_layout = QStackedLayout(self)
        stack_layout.setStackingMode(QStackedLayout.StackAll)
        self.shadow.setPixmap(QPixmap("images/shadow.png"))
        self.shadow.setVisible(False)
        self.shadow.setFixedSize(480, 10)
        self.shadow.move(0, 196)
        close_button = UICreatetor.create_close_button()
        close_button.clicked.connect(exit_app)
        close_button.move(480 - 37, 0)

        self.login_view.signal_login.connect(self.on_login)
        stack_layout.addChildWidget(self.login_view)
        stack_layout.addChildWidget(self.status_view)
        stack_layout.addChildWidget(self.shadow)
        stack_layout.addChildWidget(UICreatetor.create_banner_image())
        stack_layout.addChildWidget(close_button)

    def on_login(self):
        self.status_view.easing_in()

    def add_background_msg(self, msg):
        self.status_view.add_background_msg(msg)


class MainThread:
    def __init__(self):
        self.ui = None

    def begin_play(self, ui):
        self.ui = ui
        print("begin")
        check_thread = RestrictedAssetChecker.AssetChecker(self.ui)
        check_thread.setParent(self.ui)
        check_thread.start()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
