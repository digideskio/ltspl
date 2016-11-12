import uuid
from pyDes import *
import base64
import binascii
import struct
import requests


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

if __name__ == "__main__":
    KEY = b"O\0y\0e\0a\0"
    k = des(KEY, CBC, KEY, pad=None, padmode=PAD_PKCS5)
    data = "lantusupei|lantusupei666|"+get_mac_address()+"|2.1"
    print("str = "+data)
    p = ""
    for i in data:
        p += i
        p += chr(0)
    k = des(KEY, CBC, KEY, pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(p)
    encrptstr = base64.encodebytes(d).decode()
    result = requests.post("http://lantusupei.com:8099/api/Account/AccountLogin", None,encrptstr)
    print(result.status_code)
    print(result.text)

