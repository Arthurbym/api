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

def post_dd(url,body,header):
    res = requests.post(url,json=body,headers=header).text
    print(res)


def get_external_ip():
    try:
        ip = requests.get('https://ident.me').text.strip()
        return ip
    except:
        return None


import os,sys
def free_port(port):
    with os.popen('lsof -i:'+str(port)) as res:
        res = res.read().split('\n')
    result = []
    for line in res:
        temp = [i for i in line.split(' ') if i != '']
        if len(temp) > 4:
            result.append({'pid': temp[1], 'comand': temp[0], 'user': temp[2],'nmae':temp[8]})
    # print("占用{}端口的进程如下:".format(port))
    # print(result)
    if len(result)>1:
        for i in range(1,len(result)): # 每个line都是一个字典
            pid=result[i]['pid']
            result = os.popen("kill -9 "+str(pid))
            print("杀死占用{}的进程号{},成功".format(port,pid))

if __name__ == '__main__':
    # DoRequest().get_token("mtbsw1@126.com",'Mtbsw54321')
    # url = 'https://oapi.dingtalk.com/robot/send?access_token=e5dd775c201411bd5136c77e2dbc8d34f3c45a2863b7f82a62acd44d6fc47032'
    # body = {
    # "msgtype": "text",
    # "title":"api测试",
    # "text": {
    #     "content":"api测试"+"\n"+"总用例数:"+"122" +"\n"+"总通过用例数:"+"122" + "\n"+"总通过率:"+"100%"
    # },
    # "at": {
    #     "atMobiles": [
    #         "15757181215"
    #     ],
    #     "isAtAll":False #这个参数为true好像是@所有人的意思
    # }}
    # header = {
    #     "Content-Type": "application/json",
    #     "Charset": "UTF-8"
    # }
    # post_dd(url,body,header)
    print(get_external_ip())