#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from common.path_data import test_suit_path, allure_data_path


if __name__ == '__main__':
    pytest.main([test_suit_path, '--alluredir', '%s' % allure_data_path, '--clean-alluredir'])



