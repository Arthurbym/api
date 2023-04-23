#!/usr/bin/env python
# -*- coding: utf-8 -*-
# md5加密
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
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

def get_file_md5(file_name):
  """
  计算文件的md5
  :param file_name:
  :return:
  """
  m = hashlib.md5()  #创建md5对象
  with open(file_name,'rb') as fobj:
    while True:
      data = fobj.read(4096)
      if not data:
        break
      m.update(data) #更新md5对象

  return m.hexdigest()  #返回md5对象


if __name__ == '__main__':
    # print(get_md5('sdas'))
    # print(get_md5('sdas'))
    # print(get_md5('sdas'))
    # time.sleep(1)
    # print(get_md5('sdas'))
    print(get_file_md5(r'D:\ApiAuto\test_data\api_doc\api_pitpat.xlsx'))
