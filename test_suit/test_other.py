#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.do_excel import DoExcel
from common.do_sql import DoSql
from common.do_request import DoRequest
import allure, pytest,time,json
from common.log import Logger
from config.config_data import headers
from common.do_md5 import get_md5

log = Logger(__name__).get_logger()

# data = DoExcel().get_api_list()

# @allure.epic('自动化接口测试')
class TestOther():
    @allure.title('取消匹配')
    def test_called(self):
        with allure.step('发起接口请求'):
            res = json.loads(DoRequest().post_url('/app/mind/match',json={"targetMileage":1600,"userId":343},headers =headers ).text)
            # uniqueCode = res["data"]['uniqueCode']
            res1 = DoRequest().post_url('/app/mind/cancel/match', json={"userId":343},headers =headers).text
        with allure.step('发起接口请求'):
            assert '"code":"200"' in res1

    # def test_home(self):
    #     headers1=headers.copy()
    #     headers1['sign']= get_md5(get_sign(headers))
    #     headers1['Content-Type'] = 'application/json'
    #     print(headers1)
    #     res = DoRequest().post_url('/app/user/loginNew',json={"emailAddress":"mtbsw2@126.com","password":get_md5('Mtbsw54321')},headers=headers1).text
    #     print(res)


if __name__ == '__main__':
    TestOther().test_home()