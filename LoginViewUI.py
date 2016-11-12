from PyQt5.QtWidgets import QWidget, QStackedLayout, \
    QVBoxLayout, QHBoxLayout, QLabel, QCheckBox
from PyQt5.QtCore import QPoint, QPropertyAnimation, QEasingCurve, pyqtSignal
import UICreatetor
from PyQt5.Qt import *
import os
import LoginTool


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

        self.msg_alert = QLabel("密码不能为空")
        self.msg_alert.setStyleSheet("background-color: rgb(242, 206, 58);"
                                "color: rgb(80, 80, 80);font: 12pt \"Microsoft YaHei UI\";")
        self.msg_alert.resize(476, 30)
        self.msg_alert.setAlignment(Qt.AlignCenter)
        self.msg_alert.move(0, 200)
        stack_layout.addChildWidget(self.msg_alert)

        self.alert_anim_in = QPropertyAnimation(self.msg_alert, b"pos")
        self.alert_anim_in.setStartValue(QPoint(0, 200))
        self.alert_anim_in.setEndValue(QPoint(0, 200))
        self.alert_anim_in.setEasingCurve(QEasingCurve.OutBack)
        self.alert_anim_in.setKeyValueAt(0.05, QPoint(0, 170))
        self.alert_anim_in.setKeyValueAt(0.95, QPoint(0, 170))
        self.alert_anim_in.setDuration(8000)

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

        if os.path.exists("ac.bin"):
            with open("ac.bin", "r") as file:
                content = file.read()
                dec_str = LoginTool.decrypt(content)
                print(dec_str)
                dec_str = dec_str.replace("\x00", "")
                ups = dec_str.split("|")
                print(ups,len(ups))
                if len(ups) == 2:
                    self.username_edit.setText(ups[0])
                    self.password_edit.setText(ups[1])
                file.close()
        else:
            print("密码文件不存在")

    def show_alert(self, msg):
        self.msg_alert.setText(msg)
        self.alert_anim_in.stop()
        self.alert_anim_in.start()

    def create_login_content(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        self.username_edit = UICreatetor.create_username_input()
        layout.addWidget(self.username_edit, 0, Qt.AlignCenter)

        self.password_edit = UICreatetor.create_password_input()
        self.password_edit.returnPressed.connect(self.on_login_clicked)
        layout.addWidget(self.password_edit, 0, Qt.AlignCenter)

        center_layout = QHBoxLayout()
        self.save_paw_check = QCheckBox("保存密码")
        self.save_paw_check.setChecked(True)
        self.save_paw_check.setStyleSheet("font: 75 11pt \"Microsoft YaHei UI\";color: rgb(134, 134, 134);")
        center_layout.addWidget(self.save_paw_check)
        forget = QLabel("忘记密码")
        # forget.addAction()
        forget.setStyleSheet("font: 75 11pt \"Microsoft YaHei UI\";color: rgb(108, 202, 218);padding-right:0px")
        center_layout.addWidget(forget, 0, Qt.AlignRight)
        layout.addLayout(center_layout)
        layout.addSpacing(10)

        login_btn = UICreatetor.create_login_button()
        login_btn.clicked.connect(self.on_login_clicked)
        layout.addWidget(login_btn, 0, Qt.AlignCenter)
        login_btn.setFixedSize(188, 38)
        layout.addStretch()
        widget.resize(290, 200)
        return widget

    def on_login_clicked(self):
        self.signal_login.emit()

    def easing_in(self):
        self.anim_in.start()

    def easing_out(self):
        self.anim_out.start()
