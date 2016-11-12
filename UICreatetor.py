from PyQt5.QtWidgets import QLabel,\
    QLineEdit, QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap


def create_background(w=476, h=200):
    bottom_image = QLabel()  # 底部白色背景
    bottom_image.resize(w, h)
    bottom_image.setPixmap(QPixmap("images/ButtomArea.png"))
    shadow  = QGraphicsDropShadowEffect(bottom_image)
    return bottom_image


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


def create_login_button():
    login_btn = QPushButton()
    login_btn.setStyleSheet(
        "QPushButton{background-image: url(images/login_N.png);"
        "border:0px} QPushButton:hover{background-image: url(images/login_H.png);}")
    return login_btn


def create_close_button():
    btn = QPushButton()
    btn.setStyleSheet(
        "QPushButton{background-image: url(images/close_N.png);"
        "border:0px} QPushButton:hover{background-image: url(images/close_H.png);}")
    btn.resize(37, 31)
    return btn


def create_banner_image():
    banner_image = QLabel()  # 顶部背景
    banner_image.resize(480, 200)
    pixel_map = QPixmap("images/Banner.png")
    banner_image.setPixmap(pixel_map)
    return banner_image
