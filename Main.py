from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os

class MainWin(QWidget):
	def __init__(self):
		super(MainWin, self).__init__()
		self.setWindowTitle("Hello World")
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.pre_pos = None
		self.resize(480, 460)

		stack_layout = QStackedLayout()

		banner_image = QLabel(self)  # 顶部背景
		buttom_image = QLabel(self)  # 底部白色背景
		banner_image.resize(480, 200)
		buttom_image.resize(480, 200)
		buttom_image.move(0, 200)
		pixel_map = QPixmap("images/Banner.png")
		buttom_bg = QPixmap("images/ButtomArea.png")
		banner_image.setPixmap(pixel_map)
		buttom_image.setPixmap(buttom_bg)

		self.anim = QPropertyAnimation(buttom_image, b"geometry")
		self.anim.setDuration(1500)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.setLayout(stack_layout)

	def onAddToScreen(self):
		self.anim.setStartValue(QRect(0,200,480,0))
		self.anim.setEasingCurve(QEasingCurve.InOutBounce)
		self.anim.setKeyValueAt(0.5, QRect(0,200,480,0))
		self.anim.setEndValue(QRect(0,200,480,206))
		self.anim.start()

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
