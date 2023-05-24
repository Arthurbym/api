import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import os, time,sys,platform
import ctypes

# 当前时间
current_time = time.strftime('%Y-%m-%d')
real_current_time =time.strftime('%Y-%m-%d-%H-%M-%S')
# 获取当前文件绝对路径
abs_path = os.path.abspath(__file__)
# 获取项目根目录路径
sys_pla = platform.system()
if sys_pla == "Windows":
    pro_path = str(abs_path).split("common\path_data.py")[0]
elif sys_pla == "Linux":
    pro_path = str(abs_path).split("common/path_data.py")[0]
else:
    pro_path = str(abs_path).split("common\path_data.py")[0]
# 配置文件存放路径
config_path = os.path.join(pro_path, 'config')
# 拼接日志文件路径
log_path = os.path.join(pro_path, 'report', 'log')
# 测试用例路径
test_suit_path = os.path.join(pro_path, 'test_suit')
# 报告路径
report_path = os.path.join(pro_path, 'report')
# allure测试数据地址
allure_data_path = os.path.join(pro_path, 'report', 'allure', 'allure%s' % real_current_time, 'allure_data')
# allure报告地址
allure_report_path = os.path.join(pro_path, 'report', 'allure', 'allure%s' % real_current_time, 'allure_report')
# 测试数据路径
test_data_Path = os.path.join(pro_path, 'test_data', 'api_doc')
# 安卓包路径
test_data_apk_path = os.path.join(pro_path, 'test_data', 'apk')
# ios包路径
test_data_app_path = os.path.join(pro_path, 'test_data', 'app')
# yaml路径
test_data_yaml_path = os.path.join(pro_path, 'test_data', 'yaml')
# 截图路径
image_path = os.path.join(pro_path, 'report', 'pic', '%spic' % real_current_time)

# 连接appium手机参数,官方文档地址:https://www.kancloud.cn/testerhome/appium_docs_cn/2001853
# andriod_ds = {"appActivity": ".ui.SplashActivity", "noReset": True, "udid": "127.0.0.1:62001",
#               "appPackge": "com.linzi.sport",
#               "deviceName": "192.168.4.232:5555", "automationName": "appium", "platformName": "Android"
#               }
# android_ds = {
#     "deviceName": "127.0.0.1:62001",  # 手机设备名称,可填可不填
#     "automationName": "uiAutomator2",  # 指定自动化引擎
#     "platformName": "Android",  # 使用的手机操作系统
#     "platformVersion": "10",  # 手机操作系统的版本
# "appPackge": "com.linzi.sport",  # 被测软件包名
# "appActivity": ".ui.SplashActivity",  # Activity 的名字是指从你的包中所要启动的 Android acticity
# "appPackge": "com.eg.android.AlipayGphone",  # 被测软件包名
# "appActivity": ".AlipayLogin",  # Activity 的名字是指从你的包中所要启动的 Android acticity
# "resetKeyboard": True,  # 在设定了 unicodeKeyboard 关键字的 Unicode 测试结束后，重置输入法到原有状态。如果单独使用，将会被忽略。默认值为 false
# "unicodeKeyboard": True,  # 使用 Unicode 输入法。 默认值为 false
# "skipServerInstallation": True,  # 如果手机端已安装automation2 apk则会跳过安装
# "udid": "127.0.0.1:62001",  # usb连接多个设备时可连接指定手机,就是adb devices下的设备名称,远程连接时只会显示http地址,此时指定http地址无效果
# "noReset": True,  # 为True时不停止应用，不清理应用数据，不卸载应用包。为false时	测试结束后停止应用，清理应用数据，不卸载应用包。
# "systemPort": '8201',
# appium-uiautomator2-server_通常情况默认值为 8200 ，可 从8200到8299选择一个端口。对于_appium-espresso-driver，默认值为8300，端口地址可从8300到8399中选择一个
# "adbPort": "5037",  # 用来连接 ADB 服务器的端口（默认值为 5037）
# "fullReset":True, #为True时	测试结束后停止应用，清理应用数据，卸载应用包。
# "browserName":"Browser", #	做自动化时使用的浏览器名字。如果是一个应用则只需填写个空的字符串。
# "language":"chinese", #为模拟器设置语言。
# "deviceReadyTimeout	": 5,  # 用于等待模拟器或真机准备就绪的超时时间
# "androidDeviceReadyTimeout": 5  # 用于等待设备在启动应用后准备就绪的超时时间。以秒为单位。
# "uiautomator2ServerInstallTimeout": 30000,  # 等待uiAutomator2服务器安装的超时时间（以毫秒为单位）。 默认值为 20000
# "uiautomator2ServerLaunchTimeout": 30000  # 等待uiAutomator2服务器启动的超时时间（以毫秒为单位）。 默认值为 20000
# }

# ios_ds ={
#   "platformVersion": "14.4",
#   "platformName": "ios",
#   "deviceName": "iphone",
#   "automationName": "XCUITest",
#   "bundleId": "com.linzisportsmall.pitpat",
#   "usePrebuiltWDA": "false",
#   "useXctestrunFile": "false",
#   "skipLogCapture": "true",
#   "udid": "33af491e328cc38fc2a9cd8700582f63fb26fa6a",
#   "webDriverAgentUrl": "http://localhost:8200"
# }

# 被调函数名称
funcName = sys._getframe().f_code.co_name
# 被调函数所在行号
# funcNo = sys._getframe().f_back.f_lineno
# 被调函数所在文件名称
# funcFile = sys._getframe().f_code.co_filename
if __name__ == '__main__':
    print(allure_data_path)
    print(test_suit_path, allure_data_path,allure_report_path)
    print(allure_report_path)
    print(str(time.time()).split('.')[0])
    print(config_path)
    print(pro_path)
    print(abs_path)

