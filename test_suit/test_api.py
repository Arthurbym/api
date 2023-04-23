#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.do_request import DoRequest
from common.do_excel import DoExcel
from common.do_sql import DoSql
from common.do_request import DoRequest
import allure, pytest,time
from common.log import Logger

log = Logger(__name__).get_logger()

data = DoExcel().get_api_list()


# @allure.epic('自动化接口测试')
class TestApi():
    # @allure.feature("登录")
    # @allure.story('冒烟测试')
    @allure.title('{test_model}::{test_case_name}')
    @pytest.mark.parametrize(
        'test_model,test_case_name,route,api_type,headers,md5,par,before_sql,response,response_checkout,after_sql,after_sql_checkout,fix_sql',
        data)
    def test_api(self,test_model, test_case_name, route, api_type, headers, md5, par, before_sql, response, response_checkout,
                 after_sql, after_sql_checkout,fix_sql):
        with allure.step('发起接口请求'):
            # 执行前是否需要执行sql
            if before_sql != '':
                if '::' in before_sql:
                    sql_list = before_sql.split('::')
                    for i in sql_list:
                        DoSql().change_value(i)
                else:
                    DoSql().change_value(before_sql)
            # 判断接口类型
            if api_type.upper() == 'GET':
                res = DoRequest().get_url(url=route, headers=headers, params=par).text
            elif api_type.upper() == 'POST':
                res = DoRequest().post_url(url=route, headers=headers, json=par).text
            else:
                log.info('api_type : %s 类型不正确 应为post或者get'%api_type)
        with allure.step('校验'):
            log.info('assert {response_checkout} in {res}'.format(response_checkout=response_checkout,res=res))
            assert response_checkout in res
            # 是否需要sql检查
            if after_sql_checkout != '':
                sql_res = DoSql().get_value(after_sql)
                log.info('assert {sql_res} == {after_sql_checkout}'.format(sql_res=sql_res,after_sql_checkout=after_sql_checkout))
                assert sql_res == after_sql_checkout
            # 执行结束是否需要执行修复sql
            if fix_sql != '':
                # 是否存在多条sql需要执行
                if '::' in fix_sql:
                    sql_list = fix_sql.split('::')
                    for i in sql_list:
                        DoSql().change_value(i)
                else:
                    DoSql().change_value(fix_sql)




