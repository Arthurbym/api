# -*- coding: utf-8 -*-
import base64
from Crypto.Cipher import AES
from urllib import parse

AES_SECRET_KEY = '0123456789012345'  # 此处16|24|32个字符
IV = "16-Bytes--String"

# padding算法
BS = len(AES_SECRET_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    # 加密函数
    def encrypt(self, text):
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext)

    # 解密函数
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text)


if __name__ == '__main__':
    headers = {'appType': '2', 'appVersion': '206', 'email': 'mtbsw2@126.com', 'time': '1684492860000', 'uuid': 'dbc91fbd0bc5407da62264428b70c16e', 'token': 'tOiInV19rWAKpOtK2i7J868', 'sign': 'b70d4cb707ef160841ddc75f03eb2095'}
    headers = {'token': 'tO8'}
    print(str(headers['token'])[0:16])
