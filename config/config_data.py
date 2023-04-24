#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.do_config import DoConfigIni
import  time,base64
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


doc = DoConfigIni()


# 翻译走查语言
def get_conf():
    if doc.get_conf_value('environment','env')  == 'virtual':
        try:
            ip = doc.get_conf_value('ip_address_virtual','ip')
            mysqldb = {}
            mysqldb['host']  = doc.get_conf_value('mysqldb_virtual','host')
            mysqldb['port']  = int(doc.get_conf_value('mysqldb_virtual','port'))
            mysqldb['user'] = doc.get_conf_value('mysqldb_virtual','user')
            mysqldb['password'] = doc.get_conf_value('mysqldb_virtual','password')
            mysqldb['database'] = doc.get_conf_value('mysqldb_virtual','database')
            mysqldb['charset'] = doc.get_conf_value('mysqldb_virtual','charset')
            headers = {}
            headers['appType'] = doc.get_conf_value('headers', 'appType')
            headers['appVersion'] = doc.get_conf_value('headers', 'appVersion')
            headers['email'] = doc.get_conf_value('headers', 'email')
            headers['time'] = str(time.time()).split('.')[0] + '000'
            headers['uuid'] = doc.get_conf_value('headers', 'uuid')
            # headers['Content-Type'] = doc.get_conf_value('headers', 'Content-Type')
            return ip,mysqldb,headers
        except Exception:
            return 'get environment failed!!!'
    elif doc.get_conf_value('environment','env')  == 'real':
        try:
            ip = doc.get_conf_value('ip_address_real','ip')
            mysqldb = {}
            mysqldb['host']  = doc.get_conf_value('mysqldb_real','host')
            mysqldb['port']  = int(doc.get_conf_value('mysqldb_real','port'))
            mysqldb['user'] = doc.get_conf_value('mysqldb_real','user')
            mysqldb['password'] = doc.get_conf_value('mysqldb_real','password')
            mysqldb['database'] = doc.get_conf_value('mysqldb_real','database')
            mysqldb['charset'] = doc.get_conf_value('mysqldb_real','charset')
            headers = {}
            headers['appType'] = doc.get_conf_value('headers', 'appType')
            headers['appVersion'] = doc.get_conf_value('headers', 'appVersion')
            headers['email'] = doc.get_conf_value('headers', 'email')
            headers['time'] = str(time.time()).split('.')[0] + '000'
            headers['uuid'] = doc.get_conf_value('headers', 'uuid')
            # headers['Content-Type'] = doc.get_conf_value('headers', 'Content-Type')
            return ip,mysqldb,headers
        except Exception:
            return 'get environment failed!!!'

# 获取签名
def get_sign(headers):
    strhe = 'zns&'
    for i in headers.items():
        if i[0] == 'token':
            strhe = strhe + str(i[1])+'&'
        else:
            strhe = strhe+ str(i[0]) + '=' +str(i[1]) +'&'
    strhe = strhe.rstrip('&')
    print(strhe)
    return strhe


# 将原始的明文用空格填充到16字节
# def pad(data):
#     block_size = 16
#     # 数据进行 PKCS5Padding 的填充
#     pad = lambda s: (s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size))
#     data = pad(data)
#     print(data)
#     return  data

# bs = AES.block_size
# pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
# un_pad = lambda s: s[:-ord(s[len(s) - 1:])]
#
# def pading(text):
#     bs = 16
#     bytes_1 = text.encode("utf-8")
#     bytes_1 = bytes(bytes_1)
#     print('bytes_1%s'%bytes_1)
#     if len(bytes_1) <= bs:
#         times =bs-len(bytes_1)
#         for i in range(times):
#             print(bytes(str(times),"utf-8"))
#             bytes_1 += bytes(str(times),"utf-8")
#     print(bytes_1.decode("utf-8"))
#     return bytes_1.decode("utf-8")


def get_aes(contect,key):
    iv = "16-Bytes--String"
    # 加密模式，可以是CBC、CFB、ECB、OFB等模式
    mode = AES.MODE_CBC
    by_key = key.encode("utf-8")

    cipher = AES.new(by_key,mode,iv.encode("utf-8"))
    # 完成加密
    # contect.encode("utf-8")
    # pand_contect = pad(contect)
    # pand_contect = pad(contect).encode("utf-8")
    # pand_contect = bytes(pad(contect),'utf-8')
    pand_contect = pad(contect.encode(),16,style='pkcs7')
    print(pand_contect)
    # pand_contect = contect.encode("utf-8")
    # print(pand_contect)
    # print(len(pand_contect))
    AES_en_str = cipher.encrypt(pand_contect)
    # 用base64编码一下
    AES_en_str = base64.b64encode(AES_en_str)
    # 最后将密文转化成字符串
    AES_en_str = AES_en_str.decode("utf-8")
    return AES_en_str

# def aes_decrypt(key,text):
#     """
#     解密 ：偏移量为key[0:16]；先base64解，再AES解密，后取消补位
#     :param encrypted_text : 已经加密的密文
#     :return:
#     """
#     iv = "16-Bytes--String"
#     encrypted_text = b64decode(text)
#     cipher = AES.new(key=key.encode(), mode=AES.MODE_CBC, IV=iv.encode())
#     decrypted_text = cipher.decrypt(encrypted_text)
#     return un_pad(decrypted_text).decode('utf-8')



ip,mysqldb,headers = get_conf()
env = doc.get_conf_value('environment','env')


if __name__ == "__main__":
    print(ip,mysqldb,headers)
    # print(headers)
    # print(env)
    # print( str(time.time()).split('.')[0]+'000')
    print(get_sign(headers = headers))
    sd = get_aes("mtbsw4@126.com", "0123456789012345")
    print(sd)
    # print(aes_decrypt('0123456789012345',sd))
    print('m8ExrP9lMGCWygajBz2o8Q==')

    # print('d'+aes_decrypt('0123456789012345', 'm8ExrP9lMGCWygajBz2o8Q==')+'')
