#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
重写import configparser的optionxform方法，不然读取key会转换小写，
'''
import configparser


class MyConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr