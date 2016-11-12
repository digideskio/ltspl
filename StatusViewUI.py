from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGraphicsBlurEffect
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve
import UICreatetor


class StatusView(QWidget):
    def __init__(self):
        super(StatusView, self).__init__()
        self.resize(476, 200)
        stack_layout = QStackedLayout(self)
        stack_layout.setStackingMode(QStackedLayout.StackAll)
        stack_layout.addWidget(UICreatetor.create_background())

        self.anim_in = QPropertyAnimation(self, b"pos")
        self.anim_out = QPropertyAnimation(self, b"pos")
        self.anim_in.setStartValue(QPoint(2, 0))
        self.anim_in.setEndValue(QPoint(2, 200))
        self.anim_in.setKeyValueAt(0.4, QPoint(2, 0))
        self.anim_in.setEasingCurve(QEasingCurve.InOutBounce)
        self.anim_in.setDuration(1500)

        self.anim_out.setDuration(600)
        self.anim_out.setStartValue(QPoint(2, 200))
        self.anim_out.setEndValue(QPoint(2, 0))
        self.anim_out.setEasingCurve(QEasingCurve.OutExpo)

        test = QLabel("登陆成功")
        test.move(227,91)
        test.resize(60,30)
        stack_layout.addChildWidget(test)
        #stack_layout.addChildWidget(QPushButton("登陆成功"))

    def add_background_msg(self, msg):
        pass
        #self.status_edit.append("      "+msg)

    def easing_in(self):
        self.anim_in.start()

    def easing_out(self):
        self.anim_out.start()
