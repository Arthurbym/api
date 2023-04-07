# 项目介绍
利用appium开源工具封装而成的api自动化项目
   
# 环境配置
1.[allure2下载地址](https://github.com/allure-framework/allure2/releases)  
2.allure/bin路径添加至系统环境path中。  
3.pycharm/bin路径添加至系统环境path中。  
   
# 项目结构
common：存放公用方法  
config：存放项目配置  
report：存放测试结果，包含日志，截图，allure报告  
test_data: 存放测试数据，包含apk,元素管理文件,yaml测试数据文件    
test_suit：存放测试用例  
pytest.ini: pytest运行配置文件  
requirements.txt: 项目依赖库文件  
run_test.py: 项目运行文件  
gitignore：存放不上传到git上的内容  


#配置文件
environment: 执行环境
ip_address_real：真实环境ip地址
mysqldb_real：真实环境数据库
ip_address_virtual：虚拟环境ip地址
mysqldb_virtual：虚拟环境数据库
headers：通用请求头






