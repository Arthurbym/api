import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time, os, logging
from common.path_data import log_path

class Logger(object):
    def __init__(self, logger_name='automation', cmd_level=logging.INFO, file_level=logging.INFO):
        '''

        :param logger_ame:日志名
        :param cmd_level:日志等级
        :param file_level:日志文件等级
        '''
        self.logger_name = logger_name
        self.file_level = file_level
        self.cmd_level = cmd_level

    def get_logger(self):
        '''

        :return: logger
        '''
        try:
            # 设置日志名
            self.logger = logging.getLogger(self.logger_name)
            # 设置日志等级
            self.logger.setLevel(self.file_level)
            # 设置日志格式
            fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(filename)s %(lineno)d] [%(message)s]")
            # 设置文件路径
            self.current_time = time.strftime("%Y-%m-%d")
            self.file_path = os.path.join(log_path, '%s.log' % self.current_time)
            if os.path.exists(log_path):
                pass
            else:
                os.makedirs(log_path)
            # self.file_path = log_path + '\\' + self.current_time + '.log'
            # 设置文件输出路径，格式，等级
            fh = logging.FileHandler(self.file_path, encoding='UTF-8')
            fh.setFormatter(fmt)
            fh.setLevel(self.file_level)
            # 添加文件输出
            self.logger.addHandler(fh)
        except Exception:
            print("cant create logger")
            raise Exception
        else:
            return self.logger


if __name__ == "__main__":
    log = Logger(__name__).get_logger()
