from common.path_data import test_data_Path
import xlrd, os,json
from common.log import Logger
from common.do_md5 import get_md5
log = Logger(__name__).get_logger()


class DoExcel(object):

    def __init__(self, fileName='api_pitpat.xlsx'):
        '''

        :param fileName:xlsx文件名称
        :param sheetName:表名称
        '''
        try:
            self.dataFile = os.path.join(test_data_Path, fileName)
            # 打开excel
            self.workbook = xlrd.open_workbook(self.dataFile)

            # self.sheetName = xlrd.open_workbook(self.dataFile).sheet_by_name(sheetName)
        except Exception:
            log.exception('get %s failed ' % self.dataFile)
            raise
        else:
            log.info('get %s succeed ' % self.dataFile)

    def values_strip(self, values):
        '''

        :param values: 数组
        :return:格式化左右边空格
        '''
        new_values = []
        for i in values:
            if isinstance(i,str):
                i = i.strip()
            new_values.append(i)
        return new_values

    def get_sheet_row_values(self, sheetName, row):
        '''

        :param sheetName: 表名
        :param row: 行号
        :return: 行值
        '''
        try:
            # 打开表
            sheetName = self.workbook.sheet_by_name(sheetName)
            values = sheetName.row_values(row)
            new_values = self.values_strip(values)
        except Exception:
            log.exception("get values failed!")
        else:
            log.info("get values succeed!")
            return new_values

    def get_sheet_column_values(self, sheetName, column):
        '''

        :param sheetName:表名
        :param column:列号
        :return:列值
        '''
        try:
            # 打开表
            sheetName = self.workbook.sheet_by_name(sheetName)
            values = sheetName.col_values(column)
        except Exception:
            log.exception("get values failed!")
        else:
            log.info("get values succeed!")
            return values

    def get_cell_value(self, sheetName, row, column):
        '''

        :param sheetName: 表名
        :param row: 单元格行号
        :param column:单元格列号
        :return:单元格值
        '''
        try:
            sheetName = self.workbook.sheet_by_name(sheetName)
            value = sheetName.cell(row, column).value
        except Exception:
            log.exception('get value %s,%s in sheetName %sfailed' % (row, column, sheetName))
            raise
        else:
            log.info('get value %s,%s in sheetName %s succeed' % (row, column, sheetName))
            return value

    def get_sheet_json(self, sheetName):
        '''

        :param sheetName:表名
        :return:
        '''
        try:
            sheet_json = {}
            sheet_json[sheetName] = {}
            sheet = self.workbook.sheet_by_name(sheetName)
            rows = sheet.nrows
            keys = self.get_sheet_row_values(sheetName, 0)
            for r in range(1, rows):
                cell_value_json = {}
                row_values = self.get_sheet_row_values(sheetName, r)
                cell_nrows = len(row_values)
                for n in range(cell_nrows):
                    cell_value_json[keys[n]] = row_values[n]
                sheet_json[sheetName][row_values[0]] = cell_value_json
                # sheet_json[sheetName]['values'] = cell_value_json1
        except Exception:
            log.exception("get sheet %s failed！" % sheetName)
        else:
            log.info("get sheet %s succeed！" % sheetName)
            return sheet_json

    def get_file_json(self):
        '''

        :return: 单文件json
        '''
        try:
            sheet_names = self.workbook.sheet_names()
            self.file_json = {}
            for n in range(len(sheet_names)):
                value = self.get_sheet_json(sheet_names[n])
                self.file_json.update(value)
        except Exception:
            log.exception("get file %s failed！" % self.dataFile)
        else:
            log.info("get file %s succeed！" % self.dataFile)
            return self.file_json


    def get_api_list(self,sheetName='login'):
        # api参数化 返回元组
        try:
            api_list = []
            sheet = self.workbook.sheet_by_name(sheetName)
            rows = sheet.nrows
            for i in range(1,rows):
                rows_value = self.get_sheet_row_values(sheetName,i)
                if rows_value[4] != '':
                    rows_value[5] = json.loads(rows_value[5])
                    re = get_md5(rows_value[5][rows_value[4]])
                    rows_value[5][rows_value[4]] = re
                    api_list.append(rows_value)
                else:
                    rows_value[5] = json.loads(rows_value[5])
                    api_list.append(rows_value)
        except Exception:
            log.exception('get api_list failed!!!')
        else:
            log.info('get api_list : %s succeed!!!'%str(api_list))
            return api_list




if __name__ == "__main__":
    # file_j = DoExcel().get_file_json()
    # print(file_j['login']['正常登录'])
    # asd =json.loads(file_j['login']['正常登录']['par'])
    # print(asd['password'])
    # print(type(asd['password']))
    # print(type(json.loads(file_j['login']['正常登录']['par'])))
    # print(type(file_j['login']['正常登录']['par']))
    print(DoExcel().get_api_list())
