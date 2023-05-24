import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.do_md5 import get_md5


def get_sign(headers):
    # 将请求参数拼接成字符串，再进行md5加密
    strSign = 'zns&'
    for i in headers.items():
        if i[0] == 'token':
            strSign = strSign  + str(i[1]) + '&'
        else:
            strSign = strSign+ str(i[0]) + '=' +str(i[1]) +'&'
    strSign = strSign.rstrip('&')
    sign = get_md5(strSign)
    return sign

if __name__ == '__main__':
    pass