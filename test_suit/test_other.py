#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.do_excel import DoExcel
from common.do_sql import DoSql
from common.do_request import DoRequest
import allure, pytest,time,json
from common.log import Logger
from config.config_data import headers


log = Logger(__name__).get_logger()

data = DoExcel().get_api_list()

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

