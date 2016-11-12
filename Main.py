from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from LoginViewUI import LoginView
from StatusViewUI import StatusView
import UICreatetor
import RestrictedAssetChecker
from EventDispacher import GEventDispatcher
from EventDispacher import Event
import LoginTool
import json
import subprocess

def exit_app():
    QApplication.exit()


class MainWin(QWidget):
    signal_login_success = pyqtSignal()

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
        usn = self.login_view.username_edit.text().replace(" ", "")
        paw = self.login_view.password_edit.text().replace(" ", "")
        if len(usn) is 0 or len(paw) is 0:
            self.login_view.show_alert("用户名和密码不能为空")
            return
        login_result = LoginTool.login(usn, paw)
        if login_result is None:
            self.login_view.show_alert("连接服务器失败")
            return
        if login_result.status_code == 200:
            print(login_result.text)
            js_data = json.loads(login_result.text)
            print(js_data["Success"])
            if js_data["Success"] is False:
                self.login_view.show_alert(js_data['Msg'])
                return
            else:
                ups = usn + "|" + paw
                self.login_success(js_data, ups)

        else:
            self.login_view.show("连接服务器失败")
            return

    def add_background_msg(self, msg):
        self.status_view.add_background_msg(msg)

    def login_success(self,js_data,ups):
        print("登陆成功 ", js_data['Msg'])
        if self.login_view.save_paw_check.isChecked():
            print("保存密码", ups)
            secstr = LoginTool.encrypt(ups.encode())
            print(secstr)
            ac_path = os.path.join(os.getcwd(), "ac.bin")
            fd = open(ac_path, "w")
            fd.write(secstr)
            fd.close()
        else:
            try:
                os.remove("ac.bin")
            except Exception as err:
                pass
        self.login_view.easing_out()
        self.status_view.easing_in()
        user_config_path = os.getcwd()+"\\Project\\Plugins\\HouseEditionPlugin\\Resources"
        print(user_config_path)
        if not os.path.exists(user_config_path):
            os.makedirs(user_config_path)
        with open(user_config_path+"\\User.json", "w") as file:
            file.write(" {\"Success\":\"true\",\"Msg\":\""
                       + js_data['Msg']+"\",\"UserID\":\""+ups.split("|")[0] +"\",\"Version\":\"3.33\"}")
            file.close()

            ue_path = os.getcwd()+"\\Engine\\Binaries\\\Win64\\UE4Editor.exe"
            ltsp_path ="\""+os.getcwd() +"\\Project\\HomeDesignIII.uproject\""
            map_path = "TempMap.umap"
            cmd = ue_path+" "+ltsp_path+" "+map_path
            print(cmd)
            subprocess.Popen(cmd)

class MainThread(QObject):
    def __init__(self):
        super(MainThread,self).__init__()
        self.ui = None

    def begin_play(self, ui):
        self.ui = ui
        self.ui.signal_login_success.connect(self.login_success)
        self.check_thread = RestrictedAssetChecker.AssetChecker(self.ui)
        self.check_thread.signal_message.connect(self.ui.add_background_msg)
        self.check_thread.setParent(self.ui)
        GEventDispatcher.addEventListener("login_success",self.login_success)

    def login_success(self, _):
        self.check_thread.start()
        GEventDispatcher.removeEventListener("login_success", self.login_success)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
