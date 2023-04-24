#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests,random
from common.log import Logger
from config.config_data import ip

log = Logger(__name__).get_logger()


class DoRequest():
    def __init__(self):
        pass

    def get_url(self, url, **par):
        # url : /app/runActivity/startRun
        try:
            url = ip+ url
            log.info(url)
            res = requests.get(url, **par)
        except Exception:
            log.exception('error！ url:%s,par:%s ' % (url, par))
        else:
            log.info('get url:%s,par:%s succeed!,response = %s' % (url, par,res.text))
            return res

    def post_url(self, url, json=None, **kwargs):
        # url : /app/runActivity/startRun
        try:
            url = ip + url
            res = requests.post(url, json=json, **kwargs)

        except Exception:
            log.exception('error！ url:%s,data:%s ' % (url, json))
        else:
            log.info('post url:%s,par:%s succeed! ,response = %s' % (url, json,res.text))
            return res


if __name__ == '__main__':
    pass