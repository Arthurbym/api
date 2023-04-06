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


#注意事项

#### 切换appium连接配置
appium连接配置在config/config.ini文件中修改android_ds  
#### 修改翻译走查的语言
在config/config.ini文件中修改project中的language，例如要测试日文，
可修改language为Japanese(elements.xlsx中要有对应的表头，text_Japanese)  
#### 修改pytest运行时截图规则
在config/config.ini文件中修改allure中的pic，
allure报告截图，默认all=失败成功都截图，pass=成功截图，fail=失败截图  
#### 修改pytest运行系统
在config/config.ini文件中修改project中的system，system=android或者ios  




