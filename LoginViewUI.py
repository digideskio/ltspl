from PyQt5.QtWidgets import QWidget, QStackedLayout, \
    QVBoxLayout, QHBoxLayout, QLabel, QCheckBox
from PyQt5.QtCore import QPoint, QPropertyAnimation, QEasingCurve, pyqtSignal
import UICreatetor
from PyQt5.Qt import *


class LoginView(QWidget):
    signal_login = pyqtSignal()
    def __init__(self):
        super(LoginView, self).__init__()
        self.resize(476, 200)
        stack_layout = QStackedLayout(self)
        stack_layout.setStackingMode(QStackedLayout.StackAll)
        stack_layout.addChildWidget(UICreatetor.create_background())

        content = self.create_login_content()
        content.move( self.width()-content.width() >> 1, self.height()-content.height() >> 1 )
        stack_layout.addChildWidget(content)

        self.anim_in = QPropertyAnimation(self, b"pos")
        self.anim_out = QPropertyAnimation(self, b"pos")
        self.anim_in.setStartValue(QPoint(2, 0))
        self.anim_in.setEndValue(QPoint(2, 200))
        self.anim_in.setKeyValueAt(0.5, QPoint(2, 0))
        self.anim_in.setEasingCurve(QEasingCurve.InOutBounce)
        self.anim_in.setDuration(2000)

        self.anim_out.setDuration(500)
        self.anim_out.setStartValue(QPoint(2, 200))
        self.anim_out.setEndValue(QPoint(2, 0))
        self.anim_out.setEasingCurve(QEasingCurve.OutExpo)

    def create_login_content(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        username_edit = UICreatetor.create_username_input()
        layout.addWidget(username_edit, 0, Qt.AlignCenter)
        password_edit = UICreatetor.create_password_input()
        layout.addWidget(password_edit, 0, Qt.AlignCenter)

        center_layout = QHBoxLayout()
        save_paw_check = QCheckBox("保存密码")
        save_paw_check.setStyleSheet("font: 75 11pt \"Microsoft YaHei UI\";color: rgb(134, 134, 134);")
        center_layout.addWidget(save_paw_check)
        forget = QLabel("忘记密码")
        # forget.addAction()
        forget.setStyleSheet("font: 75 11pt \"Microsoft YaHei UI\";color: rgb(108, 202, 218);padding-right:0px")
        center_layout.addWidget(forget, 0, Qt.AlignRight)
        layout.addLayout(center_layout)
        layout.addSpacing(15)

        login_btn = UICreatetor.create_login_button()
        login_btn.clicked.connect(self.on_login_clicked)
        layout.addWidget(login_btn, 0, Qt.AlignCenter)
        login_btn.setFixedSize(188, 38)
        layout.addStretch()
        widget.resize(290, 200)
        return widget

    def on_login_clicked(self):
        self.easing_out()
        self.signal_login.emit()

    def easing_in(self):
        self.anim_in.start()

    def easing_out(self):
        self.anim_out.start()
