#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.do_request import DoRequest
from common.do_excel import DoExcel
from common.do_sql import DoSql
from common.do_request import DoRequest
import allure, pytest
from common.log import Logger

log = Logger(__name__).get_logger()

data = DoExcel().get_api_list()


@allure.epic('登录')
class TestApi():
    @allure.feature("登录")
    @allure.story('冒烟测试')
    @allure.title('{test_case_name}')
    @pytest.mark.parametrize(
        'test_case_name,route,api_type,headers,md5,par,before_sql,response,response_checkout,after_sql,after_sql_checkout,fix_sql',
        data)
    def test_api(self, test_case_name, route, api_type, headers, md5, par, before_sql, response, response_checkout,
                 after_sql, after_sql_checkout,fix_sql):
        with allure.step('发起接口请求'):
            if before_sql != '':
                DoSql().change_value(before_sql)
            if api_type == 'get':
                res = DoRequest().get_url(url=route, headers=headers, params=par).text
            elif api_type == 'post':
                res = DoRequest().post_url(url=route, headers=headers, json=par).text
            # if after_sql_checkout != '':
            #     sql_res = DoSql().get_value(after_sql)
        with allure.step('校验'):
            log.info('assert {response_checkout} in {res}'.format(response_checkout=response_checkout,res=res))
            assert response_checkout in res
            if after_sql_checkout != '':
                sql_res = DoSql().get_value(after_sql)
                log.info('assert {sql_res} == {after_sql_checkout}'.format(sql_res=sql_res,after_sql_checkout=after_sql_checkout))
                assert sql_res == after_sql_checkout
            if fix_sql != '':
                DoSql().change_value(fix_sql)




