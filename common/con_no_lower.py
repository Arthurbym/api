#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
重写import configparser的optionxform方法，不然读取key会转换小写，
'''
import configparser
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MyConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr