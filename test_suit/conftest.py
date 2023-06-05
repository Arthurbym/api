import pytest, os
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.path_data import allure_data_path, allure_report_path, real_current_time
from common.log import Logger
from config.config_data import *
from common.do_request import post_dd,get_external_ip,free_port


log = Logger(__name__).get_logger()


# 初始化driver
# @pytest.fixture(scope='session', autouse=True)
# def get_driver():
#     '''
#     :return:pp对象，直接调用pp中的方法
#     '''
#     global driver
#     global pp
#     if system == 'ios':
#         sds = ios_ds
#     elif system == 'android':
#         sds = android_ds
#     else:
#         log.info('config.ini project system value is wrong!')
#         sds = None
#     driver = AppiumDriver().get_andriod_driver(ds=sds)
#     pp = PitPat(driver)
#     # if system == 'android':
#     #     pp.set_language()
#     pp.auto_reset()
#     # pp.auto_ios_reset()
#     yield pp
#     driver.quit()



#
# @pytest.fixture(scope='session', autouse=True)
# def elements_json():
#     '''
#     初始化元素信息
#     '''
#     global file_json_value
#     file_json_value = DoExcel().get_file_json()
#     return file_json_value

#
# @pytest.fixture(scope='function', autouse=True)
# def app_reset_full():
#     '''
#     app端全部初始化
#     '''
#     yield
#     pp.auto_reset()



# 生成environment.propertie文件，需要放到alure
def pytest_sessionfinish(session):
    if env == 'virtual':
        with open("{}\\report\\allure\\allure{}\\allure_data\\environment.properties".format(session.config.rootdir,
                                                                                             real_current_time),
                  "w")as f:
            f.write(
                "ip={ip}".format(ip=ip))
            f.close()
    elif env == 'real':
        with open("{}\\report\\allure\\allure{}\\allure_data\\environment.properties".format(session.config.rootdir,
                                                                                             real_current_time),
                  "w")as f:
            f.write(
                 "ip={ip}".format(ip=ip))
            f.close()
    else:
        raise Exception('system are not allow!')
    os.popen('allure generate %s -o %s --clean' % (allure_data_path, allure_report_path))
    free_port(8889)
    time.sleep(60)
    os.popen('allure serve -h 0.0.0.0 -p 8889 %s' % (allure_report_path))
    log.info('generate allure report succeed!')
    ext_ip = get_external_ip()
    url = 'https://oapi.dingtalk.com/robot/send?access_token=e5dd775c201411bd5136c77e2dbc8d34f3c45a2863b7f82a62acd44d6fc47032'
    body = {
        "msgtype": "text",
        "title": "api测试",
        "text": {
            "content": "自动化api测试已完成" + "\n" + "网址路径:" + "http://%s:8889"%ext_ip
        },
        "at": {
            "atMobiles": [
                "15757181215"
            ],
            "isAtAll": False  # 这个参数为true好像是@所有人的意思
        }}
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    post_dd(url, body, header)


# allure generate D:\api\report\allure\allure2023-05-23-23-00-31\allure_data -o D:\api\report\allure\allure2023-05-23-23-00-31\allure_report --clean
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item):
#     '''
#     hook pytest失败
#     :param item:
#     :param call:
#     :return:
#     '''
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     suit_name = rep.nodeid
#     # we only look at actual failing test calls, not setup/teardown
#     # 当失败时截图
#     # if rep.when == "call" and rep.failed:
#     # 执行测试用例截图
#     if rep.when == "call":
#         if pic == 'all':
#             # mode = "a" if os.path.exists("failures") else "w"
#             # with open("failures", mode) as f:
#             #     # let's also access a fixture for the fun of it
#             #     if "tmpdir" in item.fixturenames:
#             #         extra = " (%s)" % item.funcargs["tmpdir"]
#             #     else:
#             #         extra = ""
#             #     f.write(rep.nodeid + extra + "\n")
#             pp.set_picture()  # 调用截图函数
#         elif pic == 'fail':
#             if rep.failed:
#                 pp.set_picture()
#         elif pic == 'pass':
#             if rep.passed:
#                 pp.set_picture()
#         else:
#             raise Exception('config.ini section: allure pic value wrong! please write \'all\',\'pass\',\'fail\'')
#     else:
#         pass


if __name__ == "__main__":
    print('allure generate %s -o %s --clean' % (allure_data_path, allure_report_path))
    po = os.popen('allure generate %s -o %s --clean' % (allure_data_path, allure_report_path))
    # po = os.popen(r"allure generate D:/AndriodUiAuto/report/allure/allure_data -o D:/AndriodUiAuto/report/allure/allure_report --clean")
    # po = os.popen('adb devices')
    msg = po.buffer.read().decode('utf-8')
    print(msg)
