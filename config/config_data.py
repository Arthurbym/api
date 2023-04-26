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
from Crypto.Util.Padding import pad,unpad


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
# def get_sign(headers):
#     strhe = 'zns&'
#     for i in headers.items():
#         if i[0] == 'token':
#             strhe = strhe + str(i[1])+'&'
#         else:
#             strhe = strhe+ str(i[0]) + '=' +str(i[1]) +'&'
#     strhe = strhe.rstrip('&')
#     print(strhe)
#     return strhe


def get_aes(contect,key):
    iv = "16-Bytes--String"
    # 加密模式，可以是CBC、CFB、ECB、OFB等模式
    mode = AES.MODE_CBC
    by_key = pad(key.encode(),block_size=16)
    # by_key = key.encode("utf-8")
    cipher = AES.new(by_key,mode,iv.encode("utf-8"))
    # 完成加密
    pand_contect = pad(contect.encode(),16,style='pkcs7')
    AES_en_str = cipher.encrypt(pand_contect)
    # 用base64编码一下
    AES_en_str = base64.b64encode(AES_en_str)
    # 最后将密文转化成字符串
    AES_en_str = AES_en_str.decode("utf-8")
    return AES_en_str

def aes_decrypt(encrypt_data, key):
    # 解密过程和加密过程相反
    key = pad(key.encode(), block_size=16,style='pkcs7')
    aes = AES.new(key, AES.MODE_CBC,IV='16-Bytes--String'.encode())
    b64_data = base64.decodebytes(encrypt_data.encode(encoding='utf-8'))
    # 解密
    decrypt = aes.decrypt(b64_data)
    # 去掉补齐位，并转换成字符串
    decrypt_str = unpad(decrypt, block_size=16, style='pkcs7').decode(encoding='utf-8')
    return decrypt_str



ip,mysqldb,headers = get_conf()
env = doc.get_conf_value('environment','env')


if __name__ == "__main__":
    print(ip,mysqldb,headers)
    # print(headers)
    # print(env)
    # print( str(time.time()).split('.')[0]+'000')
    # print(get_sign(headers = headers))
    sydsa='{"code":"200","msg":"success","data":{"versionCode":"","releaseContent":"","releaseName":"","rnReleaseZipUrl":"","rnReleaseZipMd5":"","minVersion":null,"maxVersion":null,"appType":"","gmtRelease":null,"configJson":""}}'
    sd = get_aes("mtbsw", "0123456789012345")
    print(sd)
    print(aes_decrypt(sd,'0123456789012345'))
    sd1 = get_aes(sydsa, "012345678901234511232")
    print(sd1)
    print(aes_decrypt(sd1, '012345678901234511232'))
    print(sydsa ==aes_decrypt(sd1, '012345678901234511232') )
    # print('m8ExrP9lMGCWygajBz2o8Q==')

    # print('d'+aes_decrypt('0123456789012345', 'm8ExrP9lMGCWygajBz2o8Q==')+'')
