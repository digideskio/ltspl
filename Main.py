from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os


def create_close_button():
    btn = QPushButton()
    btn.setStyleSheet(
        "QPushButton{background-image: url(images/close_N.png);"
        "border:0px} QPushButton:hover{background-image: url(images/close_H.png);}")
    btn.resize(37, 31)
    btn.clicked.connect(exit_app)
    return btn


def create_login_content():
    widget = QWidget()
    layout = QVBoxLayout(widget)
    username_edit = create_username_input()
    layout.addWidget(username_edit, 0, Qt.AlignCenter)
    password_edit = create_password_input()
    layout.addWidget(password_edit, 0, Qt.AlignCenter)

    center_layout = QHBoxLayout()
    save_paw_check = QCheckBox("保存密码")
    save_paw_check.setStyleSheet("font: 75 11pt \"Microsoft YaHei UI\";color: rgb(134, 134, 134);")
    center_layout.addWidget(save_paw_check)
    forget = QLabel("忘记密码")
    forget.setStyleSheet("font: 75 11pt \"Microsoft YaHei UI\";color: rgb(108, 202, 218);padding-right:0px")
    center_layout.addWidget(forget, 0, Qt.AlignRight)
    layout.addLayout(center_layout)
    layout.addSpacing(15)
    login_btn = QPushButton()
    login_btn.setStyleSheet(
        "QPushButton{background-image: url(images/login_N.png);"
        "border:0px} QPushButton:hover{background-image: url(images/login_H.png);}")
    layout.addWidget(login_btn, 0, Qt.AlignCenter)
    login_btn.setFixedSize(188, 38)
    layout.addStretch()
    widget.resize(290, 283)
    return widget


def create_username_input():  # 创建用户名输入框
    input_edit = QLineEdit()
    input_edit.setStyleSheet(
        "QLineEdit{border-image: url(images/username_N.png);padding-left:50px;"
        "font: 12pt 'Microsoft YaHei UI';color: rgb(132, 132, 132);}"
        "QLineEdit:hover{border-image: url(images/username_N.png);}"
        "QLineEdit:focus{border-image: url(images/username_S.png);}")
    input_edit.setFixedSize(280, 33)
    input_edit.setPlaceholderText("用户名")
    input_edit.setFrame(False)
    return input_edit


def create_password_input():  # 创建密码输入框
    input_edit = QLineEdit()
    input_edit.setStyleSheet(
        "QLineEdit{border-image: url(images/password_N.png);padding-left:50px;"
        "font: 12pt 'Microsoft YaHei UI';color: rgb(132, 132, 132);}"
        "QLineEdit:hover{border-image: url(images/password_N.png);}"
        "QLineEdit:focus{border-image: url(images/password_S.png);}")
    input_edit.setFixedSize(280, 33)
    input_edit.setFrame(False)
    input_edit.setPlaceholderText("密码")
    input_edit.setEchoMode(QLineEdit.Password)
    return input_edit


def exit_app():
    exit()


class MainWin(QWidget):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setWindowTitle("Hello World")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pre_pos = None
        self.resize(480, 460)

        stack_layout = QStackedLayout(self)
        stack_layout.setStackingMode(QStackedLayout.StackAll)
        # stack_widget = QStackedWidget(self)
        banner_image = QLabel()  # 顶部背景
        buttom_image = QLabel()  # 底部白色背景
        banner_image.resize(480, 200)
        buttom_image.resize(480, 200)
        buttom_image.move(0, 200)
        pixel_map = QPixmap("images/Banner.png")
        buttom_bg = QPixmap("images/ButtomArea.png")

        banner_image.setPixmap(pixel_map)
        buttom_image.setPixmap(buttom_bg)
        stack_layout.addChildWidget(buttom_image)


        login_content = create_login_content()
        login_content.move(self.width()-login_content.width() >> 1, 203)
        stack_layout.addChildWidget(login_content)
        self.setLayout(stack_layout)
        stack_layout.addChildWidget(banner_image)

        self.shadow = QLabel()
        self.shadow.setPixmap(QPixmap("images/shadow.png"))
        self.shadow.setVisible(False)
        self.shadow.setFixedSize(480, 10)
        self.shadow.move(0, 200)
        stack_layout.addChildWidget(self.shadow)

        close_button = create_close_button()
        close_button.move(480 - 37, 0)
        stack_layout.addChildWidget(close_button)

        self.anim = QPropertyAnimation(buttom_image, b"geometry")
        self.login_content_anim = QPropertyAnimation(login_content, b"geometry")

    def onAddToScreen(self):

        self.anim.setDuration(2000)
        self.anim.setStartValue(QRect(2, 200, 476, 0))
        self.anim.setEasingCurve(QEasingCurve.InOutBounce)
        self.anim.setKeyValueAt(0.5, QRect(2, 200, 476, 0))
        self.anim.setEndValue(QRect(2, 200, 476, 206))
        self.anim.start()

        self.login_content_anim.setDuration(2000)
        self.login_content_anim.setStartValue(QRect(102, 0, 290, 283))
        self.login_content_anim.setEndValue(QRect(102, 213, 290, 283))
        self.login_content_anim.setKeyValueAt(0.5, QRect(102, 0, 290, 283))
        self.login_content_anim.setEasingCurve(QEasingCurve.InOutBounce)
        self.login_content_anim.start()

        self.shadow.setVisible(True)

    def show(self):
        super(MainWin, self).show()
        self.onAddToScreen()

    def mousePressEvent(self, event):
        self.pre_pos = self.pos() - event.globalPos()

    def mouseMoveEvent(self, event):
        self.move(event.globalPos() + self.pre_pos)

    def mouseReleaseEvent(self, event):
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
