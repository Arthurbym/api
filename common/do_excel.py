from common.path_data import test_data_Path
import xlrd, os, json, xlwt, time
from common.log import Logger
from common.do_md5 import get_md5
from config.config_data import headers

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
            if isinstance(i, str):
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

    def get_api_list(self, sheetName='login'):
        # api参数化 返回元组
        try:
            api_list = []
            sheet = self.workbook.sheet_by_name(sheetName)
            rows = sheet.nrows
            for i in range(1, rows):
                # 判断用例是否需要执行，默认不需要执行
                rows_value = self.get_sheet_row_values(sheetName, i)
                # if rows_value[0] == 1:
                #     del rows_value[0]
                #     is_del = 1
                # elif rows_value[0] == 0:
                #     del rows_value[0]
                #     is_del = 0
                # elif rows_value[0] == '':
                #     is_del = 1
                # else:
                #     log.exception('is_test 值错误，excel中请填写0，1或者为空')
                #     is_del = 1
                if rows_value[0] != 0:
                    del rows_value[0]
                    is_del = 1
                else:
                    del rows_value[0]
                    is_del = 0

                # 处理excel中，par转json格式，及参数转md5
                if rows_value[5] != '':
                    rows_value[6] = json.loads(rows_value[6])
                    re = get_md5(rows_value[6][rows_value[5]])
                    rows_value[6][rows_value[5]] = re
                elif rows_value[6] != '':
                    rows_value[6] = json.loads(rows_value[6])
                else:
                    rows_value[6] = {}
                # 处理excel，如为整数，float转换int
                for x in range(len(rows_value)):
                    if isinstance(rows_value[x], float):
                        if int(rows_value[x]) == rows_value[x]:
                            rows_value[x] = int(rows_value[x])
                # 处理请求头，注意excel请求头格式json{}
                if rows_value[4] != '':
                    headers1 = headers
                    jl = json.loads(rows_value[4])
                    jlt = tuple(jl.items())
                    for i in range(len(jlt)):
                        headers1[jlt[i][0]] = jlt[i][1]
                    rows_value[4] = headers1

                if is_del == 0:
                    api_list.append(rows_value)
                elif is_del == 1:
                    pass
        except Exception:
            log.exception('get api_list failed!!!')
        else:
            log.info('get api_list : %s succeed!!!' % str(api_list))
            return api_list

    def get_api_elements(self):
        # 处理yapi导出json转excel,生成excel
        times = time.strftime('%Y-%m-%d-%H-%M-%S')
        file_new = xlwt.Workbook()
        with open(r"D:\ApiAuto\test_data\api_doc\api.json", "r", encoding="utf-8") as f:
            content = json.load(f)
        for i1 in range(len(content)):
            i = content[i1]
            model_name = i['name']
            table = file_new.add_sheet('%s' % model_name)
            for x1 in range(len(i['list'])):
                x = i['list'][x1]
                query_path = x['query_path']['path']
                try:
                    req_body_other = x['req_body_other']
                except Exception:
                    req_body_other = ''
                title = x['title']
                path = x['path']
                method = x['method']
                table.write(x1, 0, query_path)
                table.write(x1, 1, title)
                table.write(x1, 2, path)
                table.write(x1, 3, method)
                table.write(x1, 4, req_body_other)
        file_new.save(r'D:\ApiAuto\test_data\api_doc\api_elements%s.xls' % times)


if __name__ == "__main__":
    # file_j = DoExcel().get_file_json()
    # print(file_j['login']['正常登录'])
    # asd =json.loads(file_j['login']['正常登录']['par'])
    # print(asd['password'])
    # print(type(asd['password']))
    # print(type(json.loads(file_j['login']['正常登录']['par'])))
    # print(type(file_j['login']['正常登录']['par']))
    print(DoExcel().get_api_list())
    # print(DoExcel().get_api_elements())
