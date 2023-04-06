#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from common.do_config import DoConfigIni
from common.path_data import test_data_apk_path, test_data_app_path

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
            return ip,mysqldb
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
            return ip,mysqldb
        except Exception:
            return 'get environment failed!!!'

ip,mysqldb = get_conf()

env = doc.get_conf_value('environment','env')

if __name__ == "__main__":
    print(ip,mysqldb)
