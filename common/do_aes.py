import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import  base64
from common.do_md5 import get_md5



def get_aes(contect,key):
    iv = "16-Bytes--String"
    # 加密模式，可以是CBC、CFB、ECB、OFB等模式
    mode = AES.MODE_CBC
    # key不要panding
    by_key = key.encode()
    cipher = AES.new(by_key,mode,iv.encode("utf-8"))
    # 完成加密
    pand_contect = pad(contect.encode(),block_size=16,style='pkcs7')
    AES_en_str = cipher.encrypt(pand_contect)
    # 用base64编码一下
    AES_en_str = base64.b64encode(AES_en_str)
    # 最后将密文转化成字符串
    AES_en_str = AES_en_str.decode("utf-8")
    return AES_en_str

def aes_decrypt(encrypt_data, key):
    # 解密过程和加密过程相反
    # key不要panding
    key = key.encode()
    aes = AES.new(key, AES.MODE_CBC,IV='16-Bytes--String'.encode())
    b64_data = base64.decodebytes(encrypt_data.encode(encoding='utf-8'))
    # 解密
    decrypt = aes.decrypt(b64_data)
    # 去掉补齐位，并转换成字符串
    decrypt_str = unpad(decrypt, block_size=16, style='pkcs7').decode(encoding='utf-8')
    return decrypt_str






if __name__ == "__main__":
    # ok案例
    # paw=get_md5('12')
    # pwd = 'weew'
    #
    # pwd_aes = get_aes(pwd,"0123456789012345")
    # print('pwd_aes:'+pwd_aes)
    # print('pwd_aes:'+aes_decrypt(pwd_aes,"0123456789012345"))
    # 线上测试
    ds = get_md5('Mtbsw5432')
    pwd1 = '{"password":"%s","emailAddress":"mtbsw5@126.com"}'%ds
    print(pwd1)

    # pwd_aes1 = get_aes('', "0123456789012345")
    # print('pwd_aes1:' + pwd_aes1)
    # print('pwd_aes1:' + aes_decrypt(pwd_aes1, "0123456789012345"))
    # print('pwd_aes1:' + aes_decrypt('mt5wyrbVvEbNfcyfL36dj2ovJWRjXkrFT7qtNqlp', "0123456789012345"))

    print('pwd_aes1:' + get_aes('', "0123456789012345"))
    print('pwd_aes1:' + get_aes(pwd1, "0123456789012345"))
    # 正常
    # print('pwd_aes1:' + aes_decrypt('74AbliJZOLy43+H4je/3FHbgw9aklNoy9F14x0XUyvU1LaedsBiJVkyZR261splrc2uX4ARVeNeEpzt/jW8e2spUsmVx1PjV5piQ+RMMAVs=', "0123456789012345"))
    #
    # print('pwd_aes1:' + aes_decrypt('gYCsJbJEk5pdo/tFBnWEBnSwKYk9wvBQFddvZqrgK7yWpCp4Z8kdmaaCiZSVlM2q5xQzsnhij/MhBM97Iv3XKG1uo08AsDR4C5+B865pVLs=', "0123456789012345"))
    # print('pwd_aes1:' + aes_decrypt('L5T2JnD4x8W04Uaf4EpOeA2s4XBKo7wKW454JumvsWS+dWmkznhSqVRtoJ1CMGxayDhM88Y0gWdzexuZ01pRrcJhyepEJCymVNW79WbyXhc=', "0123456789012345"))
    #
    # print('pwd_aes1:' + aes_decrypt('RckW49yyLRyM7tHeDgzwuutocexXpKVwTwkEBzzAPqS66/1az/u/Muht4SUgH2V139yAS41151Iykpvq1NzLxp2sSjdUEhUaxNiOkA9NR1ROgInK7/RFD661lsP/bQ6KqjaCf6k8ICa7Hp0hdwxFaEeatbM7wF4D4BRxEz5szVKh0gqxCEiH3FlNpACv7faP9QvJLC62GfZSitwD3u1g/488kiYnwaLLtsQtU4JKnlQAmN1XxC+WZ0R7pYkZRfrB9+lmaR6hnZ4R0170BHJ53HJRUazSPr804aEvqeIuDf7/NAosH+sYOzEPcWBZkrnLGOf3XGbhU8T0hk0/I6rz+Mdxx5TPjG9mAoypWUjbvE4iXxKu2TxVkCB14nGBBKuy6tLOLmucG+vazgPLxgUAqqzm0otHE5el/UfDBtuUAUUtK6hJsf4kx88tz7gvVVdK4Y8DtS6pDMfFwMzsVlXvcuP2Eizhy5Smvesd15n3sG4BEz9F9zfBC4wh9KBoXWZLHgRWRUncon0+Y+/wKhmtGBbUPMMcxtAvWWXJlG2kZLgbgYA6kmMN7JuYTF5sjKbXBXISsdTFAc3TTwmwv4rNlwbvJWnPDChJT++3m+R22quFzsSBQaobknMRPWbNHQDUPd10Z6/ybj6IGr3u3B1stY4ydQgiYY3O5dIbwc7fWjaiIdTPxEe44jhj9u5U6VpBskxqdnyiOfxJSd5pfZmWQGkrL7bHwlAcTlyEbcHaRJDupmAqtiklhBd3WjjxllUwbbtWWdAYBDNV6QTp24EtooOaYYaERScH/6pccs9qnqemKU23SPW+prO2aMRG8w2/wYQKL4pPWqeneTXaMLzcqXBM7Oo/5EKI3lI3cKybtLSEn/dpdopdz/e6zrDme6I+A8vBD8oXqhl6S0ogbzRtFQ9+zrNPlbPWdB27UN2QT6s=', "0123456789012345"))
    # print('pwd_aes1:' + aes_decrypt('y8FYNCR7thvlGdyyR/6nLk7z3l1KmCX3Q6pLH3UKQxRUDMvfDHAisbF6QeFeGGVoXBudAE1210kcr8JiQ0IS0MR+CaO1PBbauTzB0cVlhOx8yQferG7TPx1mnR8V0q0P','0123456789012345'))
    # print('pwd_aes1:' + aes_decrypt('153TO2p5QQSDog24uh2hieqCkMC1VJoHrmMb5vYwVYvdw5NVsAu9G+fBsrpYD9iKIEzyzgxPCEIAB5dKuogcnjQcEgKV/45xYImnrmA9Tx4=','0123456789012345'))
    # print('pwd_aes1:' + aes_decrypt('y8FYNCR7thvlGdyyR/6nLk7z3l1KmCX3Q6pLH3UKQxRUDMvfDHAisbF6QeFeGGVoXBudAE1210kcr8JiQ0IS0MR+CaO1PBbauTzB0cVlhOx8yQferG7TPx1mnR8V0q0P','0123456789012345'))
    print(get_aes('mtbsw2@126.com','tneD8f19s1kDZLzE'))
    print('pwd_aes1:' + aes_decrypt('y8FYNCR7thvlGdyyR/6nLk7z3l1KmCX3Q6pLH3UKQxRUDMvfDHAisbF6QeFeGGVoXBudAE1210kcr8JiQ0IS0MR+CaO1PBbauTzB0cVlhOx8yQferG7TPx1mnR8V0q0P','0123456789012345'))