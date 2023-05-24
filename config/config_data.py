#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
import os

# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.do_config import DoConfigIni
import time

doc = DoConfigIni()


# 翻译走查语言
def get_conf():
    if doc.get_conf_value('environment', 'env') == 'virtual':
        try:
            ip = doc.get_conf_value('ip_address_virtual', 'ip')
            mysqldb = {}
            mysqldb['host'] = doc.get_conf_value('mysqldb_virtual', 'host')
            mysqldb['port'] = int(doc.get_conf_value('mysqldb_virtual', 'port'))
            mysqldb['user'] = doc.get_conf_value('mysqldb_virtual', 'user')
            mysqldb['password'] = doc.get_conf_value('mysqldb_virtual', 'password')
            mysqldb['database'] = doc.get_conf_value('mysqldb_virtual', 'database')
            mysqldb['charset'] = doc.get_conf_value('mysqldb_virtual', 'charset')
            headers = {}
            headers['appType'] = doc.get_conf_value('headers', 'appType')
            headers['appVersion'] = doc.get_conf_value('headers', 'appVersion')
            headers['email'] = doc.get_conf_value('headers', 'email')
            headers['time'] = str(time.time()).split('.')[0] + '000'
            headers['uuid'] = doc.get_conf_value('headers', 'uuid')

            headers['token'] = doc.get_conf_value('headers', 'token')
            # headers['sign'] = get_sign(headers)
            # headers['Content-Type'] = doc.get_conf_value('headers', 'Content-Type')
            return ip, mysqldb, headers
        except Exception:
            return 'get environment failed!!!'
    elif doc.get_conf_value('environment', 'env') == 'real':
        try:
            ip = doc.get_conf_value('ip_address_real', 'ip')
            mysqldb = {}
            mysqldb['host'] = doc.get_conf_value('mysqldb_real', 'host')
            mysqldb['port'] = int(doc.get_conf_value('mysqldb_real', 'port'))
            mysqldb['user'] = doc.get_conf_value('mysqldb_real', 'user')
            mysqldb['password'] = doc.get_conf_value('mysqldb_real', 'password')
            mysqldb['database'] = doc.get_conf_value('mysqldb_real', 'database')
            mysqldb['charset'] = doc.get_conf_value('mysqldb_real', 'charset')
            headers = {}
            headers['appType'] = doc.get_conf_value('headers', 'appType')
            headers['appVersion'] = doc.get_conf_value('headers', 'appVersion')
            headers['email'] = doc.get_conf_value('headers', 'email')
            headers['time'] = str(time.time()).split('.')[0] + '000'
            headers['uuid'] = doc.get_conf_value('headers', 'uuid')
            # headers['Content-Type'] = doc.get_conf_value('headers', 'Content-Type')
            return ip, mysqldb, headers
        except Exception:
            return 'get environment failed!!!'
ip, mysqldb, headers = get_conf()
env = doc.get_conf_value('environment', 'env')




if __name__ == "__main__":
    # get_token_to_yaml()
    # print(ip, mysqldb, headers)
    pass
