#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests,random
from common.log import Logger
from config.config_data import ip,headers
from common.do_sign import get_sign
from common.do_md5 import get_md5
from common.do_aes import get_aes,aes_decrypt


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

    def get_token(self,email,password):
        # 请求头拷贝
        headers1 = headers.copy()
        # 获取签名
        headers1['sign'] = get_sign(headers1)
        # 构造请求头，加密，密码需要先md5加密
        pa_md5=get_md5(password)
        body={"emailAddress":email,"password":str(pa_md5)}
        body = json.dumps(body)
        body_aes = get_aes(body,'0123456789012345')
        par= {"data":body_aes}
        repspone = self.post_url('/app/user/loginNew',headers= headers1,json=par)
        try:
            # 返回体取data，data解密，解密后转json
            res_data = json.loads(repspone.text)['data']
            res_aes=aes_decrypt(res_data,'0123456789012345')
            res_json = json.loads(res_aes)
            token = res_json['token']
            log.info('get email %s token %s :'%(email,token))
            return token
        except  Exception:
            log.exception('can not get token!!!')



if __name__ == '__main__':
    DoRequest().get_token("mtbsw1@126.com",'Mtbsw54321')