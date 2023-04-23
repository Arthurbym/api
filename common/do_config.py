# import configparser
import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.con_no_lower import MyConfigParser
from common.log import Logger
from common.path_data import *

log = Logger(__name__).get_logger()


class DoConfigIni(object):

    def __init__(self, filename='config.ini'):
        '''

        :param filename: ini配置文件名
        '''
        self.cf = MyConfigParser()
        self.filename = filename
        self.config_file_path = config_path + '\\' + filename

    def get_conf_section_json(self, section):
        '''
        :return:section的json串
        '''
        try:
            ds = {}
            self.cf.read(self.config_file_path, encoding='UTF-8')
            sections_value = self.cf.options(section)
            for i in sections_value:
                value = self.get_conf_value(section, i)
                if value == 'true':
                    value = True
                elif value == 'false':
                    value = False
                ds[i] = value

        except Exception as e:
            log.info("read file [%s] for [%s]-[%s] failed , did not get the value")
            raise e
        else:
            log.info('read config value [%s] succeed! ')
            return ds

    def get_conf_value(self, section, option):
        '''

        :param section: section name
        :param option: 子项key name
        :return:子项 value
        '''
        try:
            self.cf.read(self.config_file_path, encoding='UTF-8')
            value = self.cf.get(section, option)
        except Exception as e:
            log.info("read file [%s] for [%s]-[%s] failed , did not get the value" % (self.filename, section, option))
            raise e

        else:
            log.info('read config value [%s] succeed! ' % value)
            return value

    def write_conf_value(self, section, option, value):
        '''

        :param section: section name
        :param option: 子项key name
        :param value: 子项key value
        :return:
        '''
        try:
            self.cf.add_section(section)
            self.cf.set(section, option, value)
            self.cf.write(open(self.config_file_path, 'w', encoding='UTF-8'))
        except  Exception:
            log.exception('section %s has been exist!' % section)
            raise MyConfigParser.DuplicateSectionError(section)
        else:
            log.info('write section name [%s] with value [%s] successed' % (section, value))
            pass


if __name__ == "__main__":
    pass
