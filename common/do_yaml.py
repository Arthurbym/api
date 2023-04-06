#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml, os
from common.path_data import test_data_yaml_path
from common.log import Logger

log = Logger(__name__).get_logger()


class DoYaml():
    def __init__(self, file_path=test_data_yaml_path):
        '''
        file_path：默认存放yaml文件的路径
        '''
        self.default_yaml_path = file_path

    def read_yaml(self, yaml_name='test_login_page.yaml'):
        '''
        return:单文件yaml-json
        '''
        if yaml_name.endswith('.yaml'):
            yaml_path = self.default_yaml_path + '\\' + yaml_name
        else:
            # 文件路径如test_data.test_login_page
            try:
                # test_suit.test_login_page
                new_name = yaml_name.split('.')[1]
            # 文件名称如test_login_page
            except Exception:
                yaml_path = self.default_yaml_path + '\\' + yaml_name + '.yaml'
            else:
                yaml_path = self.default_yaml_path + '\\' + new_name + '.yaml'
        with open(yaml_path, 'r', encoding='gbk') as file:
            yaml_file_json = yaml.safe_load(file)
        return yaml_file_json

    def read_yamls(self, *yaml_names):
        '''
        yaml_name:文件list
        return:多文件yaml-json
        '''
        try:
            all_yaml_file_json = {}
            for yaml_name in yaml_names:
                yaml_data = self.read_yaml(yaml_name=yaml_name)
                all_yaml_file_json[yaml_name.split('.yaml')[0]] = yaml_data
        except Exception as e:
            log.info('read all yaml data from filenames :%s failed! '%str(yaml_names))
            raise e
        else:
            log.info('read all yaml data from filenames :%s succeed! '%str(yaml_names))
            return all_yaml_file_json

    def get_file_list(self, file_path):
        '''
        file_path:路径
        返回路径下的文件list
        '''
        try:
            file_list = os.listdir(file_path)
        except Exception as e:
            log.info('read file list from path:%s failed!' % file_path)
            raise e
        else:
            return file_list

    def get_yaml_file_list(self, file_path):
        '''
        file_path:路径
        return:yaml文件list
        '''
        try:
            file_list = self.get_file_list(file_path)
            yaml_file_list = []
            for file_name in file_list:
                if file_name.endswith('.yaml'):
                    yaml_file_list.append(file_name)
        except Exception as e:
            log.info('read yaml file list from path:%s failed!' % test_data_yaml_path)
            raise e
        else:
            log.info('read yaml file list from path:%s failed!' % test_data_yaml_path)
            return yaml_file_list

    def _read_yamls(self):
        '''
        return：本项目默认路径下所有yaml——json
        '''
        try:
            list = self.get_yaml_file_list(test_data_yaml_path)
            now_yaml_file_json = self.read_yamls(*list)
        except Exception as e:
            log.info('read all yaml data from path :%s failed! '%test_data_yaml_path)
            raise e
        else:
            log.info('read all yaml data from path :%s succeed! '%test_data_yaml_path)
            return now_yaml_file_json


if __name__ == "__main__":
    dsd = DoYaml()._read_yamls()['test_login_page']
    print(dsd)
