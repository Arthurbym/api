#!/usr/bin/env python
# -*- coding: utf-8 -*-
# md5加密
import hashlib,time
def get_md5(pws=None):
    """
    主要是密码等字符串进行加密处理
    :param pws: 密码
    :return: 加密之后的结果
    """
    # 调用加密方法
    if pws is None:
        return None
    else:
        md5 = hashlib.md5(pws.encode('UTF-8'))
        return md5.hexdigest()



if __name__ == '__main__':
    print(get_md5('sdas'))
    print(get_md5('sdas'))
    print(get_md5('sdas'))
    time.sleep(1)
    print(get_md5('sdas'))
