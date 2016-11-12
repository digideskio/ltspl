from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
import time


class AssetChecker(QThread):
    signal_message = pyqtSignal(str)

    def __init__(self, target=None):
        super(AssetChecker, self).__init__()
        self.identity = None
        self.target = target
        self.asset_array = []

    def run(self):
        time.sleep(1)
        for parent, _, filenames in os.walk("C:\\Users\\xtyga\\Documents\\Unreal Projects\\LTSP4110\\Content\\RestrictedAssets"):
            for filename in filenames:
                fn = os.path.join(parent, filename)
                self.asset_array.append(fn)
                #print(os.path.join(parent, filename))
                #self.signal_message.emit(os.path.join(parent, filename))
                #time.sleep(0.001)
        print("analisisy over",len(self.asset_array))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    wk = AssetChecker()
    wk.start()
    sys.exit(app.exec_())