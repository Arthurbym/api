#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.do_request import DoRequest
from common.do_excel import DoExcel
from common.do_sql import  DoSql
from common.do_request import DoRequest
import allure,pytest

data = DoExcel().get_api_list()


@allure.epic('登录')
class TestApi():
    @allure.feature("登录")
    @allure.story('冒烟测试')
    @allure.title('正常登录')
    @pytest.mark.parametrize('test_case_name,route,api_type,headers,md5,par,before_sql,response,response_checkout,after_sql,after_sql_checkout',data)
    def test_api(self,test_case_name,route,api_type,headers,md5,par,before_sql,response,response_checkout,after_sql,after_sql_checkout):
        with allure.step('发起接口请求'):
            if before_sql != '':
                DoSql().change_value(before_sql)
            if api_type == 'get':
                res = DoRequest().get_url(url =route, headers = headers,params =par ).text

            elif api_type == 'post':
                res = DoRequest().post_url(url=route, headers=headers, json=par).text
        with allure.step('校验'):
            assert response_checkout in res



