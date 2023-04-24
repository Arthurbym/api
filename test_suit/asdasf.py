#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

sd = '{"email":"mtbsw5@126.com","email1":"mtbsw51@126.com","email2":"mtbsw513@126.com"}'
sd1 = json.loads(sd)
print(tuple(sd1.items()))
print(tuple(sd1.items())[0][1])

asd='asd:sdas'
sql_list = asd.split(':')
for i in sql_list:
    print(i)




# package com.ruze.libapp.utils.encryption;
#
# import com.amazonaws.util.Base64;
# import com.ruze.libapp.BuildConfig;
#
# import javax.crypto.*;
# import javax.crypto.spec.IvParameterSpec;
# import javax.crypto.spec.SecretKeySpec;
#
# import java.io.UnsupportedEncodingException;
# import java.security.InvalidAlgorithmParameterException;
# import java.security.InvalidKeyException;
# import java.security.NoSuchAlgorithmException;
#
# /*
#  * @author songfayuan
#  * @date 2018/12/29
#  * AES对称加密和解密工具类
#  */
# public class AesUtils {
#     private static final String IV_STRING = "16-Bytes--String";
#     private static final String charset = "UTF-8";
#
#     public static final String SIGN_PASSWORD_KEY = (BuildConfig.BUILD_TYPE.equals("release") || BuildConfig.BUILD_TYPE.equals("preview")) ? "CWzQ6UjGDC#xQ+pC" : "1234567891234567";
#     public static final String IMPLEMENTS_KEY = BuildConfig.BUILD_TYPE.equals("release") ? "0123456789012345" : "0123456789012345";
#
#     public static String encryptAES(String content, String key) throws InvalidKeyException, NoSuchAlgorithmException, NoSuchPaddingException, UnsupportedEncodingException, InvalidAlgorithmParameterException, IllegalBlockSizeException, BadPaddingException {
#
#         byte[] byteContent = content.getBytes("UTF-8");
#
#         // 注意，为了能与 iOS 统一
#         // 这里的 key 不可以使用 KeyGenerator、SecureRandom、SecretKey 生成
#         byte[] enCodeFormat = key.getBytes();
#         SecretKeySpec secretKeySpec = new SecretKeySpec(enCodeFormat, "AES");
#
#         byte[] initParam = IV_STRING.getBytes();
#         IvParameterSpec ivParameterSpec = new IvParameterSpec(initParam);
#
#         // 指定加密的算法、工作模式和填充方式
#         Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
#         cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec, ivParameterSpec);
#
#         byte[] encryptedBytes = cipher.doFinal(byteContent);
#
#         // 同样对加密后数据进行 base64 编码
#         return new String(Base64.encode(encryptedBytes));
#     }
#
#
#     /**
#      * 解密-客户端使用
#      *
#      * @param content
#      * @param key
#      * @return
#      */
#     public static String aesDecryptString(String content, String key) {
#         try {
#             byte[] encryptedBytes = Base64.decode(content.getBytes());
#             byte[] keyBytes = key.getBytes(charset);
#             byte[] decryptedBytes = aesDecryptBytes(encryptedBytes, keyBytes);
#             return new String(decryptedBytes, charset);
#         } catch (InvalidKeyException | NoSuchAlgorithmException | NoSuchPaddingException | InvalidAlgorithmParameterException | IllegalBlockSizeException | BadPaddingException | UnsupportedEncodingException e) {
#             e.printStackTrace();
#         }
#         return "";
#     }
#
#     public static byte[] aesDecryptBytes(byte[] contentBytes, byte[] keyBytes) throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, InvalidAlgorithmParameterException, IllegalBlockSizeException, BadPaddingException, UnsupportedEncodingException {
#         return cipherOperation(contentBytes, keyBytes, Cipher.DECRYPT_MODE);
#     }
#
#     private static byte[] cipherOperation(byte[] contentBytes, byte[] keyBytes, int mode) throws UnsupportedEncodingException, NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, InvalidAlgorithmParameterException, IllegalBlockSizeException, BadPaddingException {
#         SecretKeySpec secretKey = new SecretKeySpec(keyBytes, "AES");
#
#         byte[] initParam = IV_STRING.getBytes(charset);
#         IvParameterSpec ivParameterSpec = new IvParameterSpec(initParam);
#
#         Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
#         cipher.init(mode, secretKey, ivParameterSpec);
#
#         return cipher.doFinal(contentBytes);
#     }


from Crypto.Cipher import AES
from base64 import b64decode, b64encode

BLOCK_SIZE = AES.block_size
# 不足BLOCK_SIZE的补位(s可能是含中文，而中文字符utf-8编码占3个位置,gbk是2，所以需要以len(s.encode())，而不是len(s)计算补码)
pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
# 去除补位
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


class AESCipher:
    def __init__(self, secretkey: str):
        self.key = secretkey  # 密钥
        self.iv = secretkey[0:16]  # 偏移量

    def encrypt(self, text):
        """
        加密 ：先补位，再AES加密，后base64编码
        :param text: 需加密的明文
        :return:
        """
        # text = pad(text) 包pycrypto的写法，加密函数可以接受str也可以接受bytess
        text = pad(text).encode()  # 包pycryptodome 的加密函数不接受str
        cipher = AES.new(key=self.key.encode(), mode=AES.MODE_CBC, IV=self.iv.encode())
        encrypted_text = cipher.encrypt(text)
        # 进行64位的编码,返回得到加密后的bytes，decode成字符串
        return b64encode(encrypted_text).decode('utf-8')

    def decrypt(self, encrypted_text):
        """
        解密 ：偏移量为key[0:16]；先base64解，再AES解密，后取消补位
        :param encrypted_text : 已经加密的密文
        :return:
        """
        encrypted_text = b64decode(encrypted_text)
        cipher = AES.new(key=self.key.encode(), mode=AES.MODE_CBC, IV=self.iv.encode())
        decrypted_text = cipher.decrypt(encrypted_text)
        return unpad(decrypted_text).decode('utf-8')