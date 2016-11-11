python -m PyInstaller Main.py -F -w
python
import os
os.rename("dist/Main.exe","Main-New.exe")