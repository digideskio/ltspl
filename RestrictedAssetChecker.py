from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
import time


class AssetChecker(QThread):
    def __init__(self, target = None):
        super(AssetChecker, self).__init__()
        self.identity = None
        self.target = target

    def run(self):
        pass
        for parent, _, filenames in os.walk("C:\\UE4\\UE4.13.1\\Engine"):
            for filename in filenames:
                self.target.add_background_msg(os.path.join(parent, filename))
                time.sleep(0.2)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    wk = AssetChecker()
    wk.start()
    sys.exit(app.exec_())