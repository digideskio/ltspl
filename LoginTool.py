import uuid
import pyDes
import base64
import binascii
import struct
import requests


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def get_ue_version() -> str:
    return "v1"


def login(username, password):
    data = username + "|" + password + "|" + \
           get_mac_address() + "|" + get_ue_version()
    try:
        secrit = encrypt(data)
        back = requests.post("http://lantusupei.com:8099/api/Account/AccountLogin", None, secrit)
        return back
    except Exception as ex:
        return None


def create_des_tool():
    key = b"O\0y\0e\0a\0"
    return pyDes.des(key, pyDes.CBC, key, pad=None, padmode=pyDes.PAD_PKCS5)


def encrypt(arg):
    u_data = ""
    if type(arg) is bytes:
        arg = arg.decode()
    for p in arg:
        u_data += p
        u_data += chr(0)
    d = create_des_tool().encrypt(u_data)
    des_str = base64.encodebytes(d).decode()
    return des_str


def decrypt(arg):

    bs = str.encode(arg)
    de64 = base64.decodebytes(bs)
    d = create_des_tool()
    res = d.decrypt(de64)
    return res.decode("utf-8")


