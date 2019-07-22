import os
from datetime import datetime

import xlrd
from xlrd import xldate_as_tuple
from xlutils.copy import copy

DATAPATH = os.path.dirname(os.path.realpath(__file__))  # 获取项目根目录
class Excel():
    def __init__(self, filename):
        """filename = excel文件名称，row = 从excel表的第几行开始读取"""

        self.filename = filename

        self.workbook = xlrd.open_workbook(DATAPATH+
            r"/{}.xls".format(
                filename))  #加载EXCLE文件

        self.table = self.workbook.sheets()[0]  #获取文件sheet

        self.nrows = self.table.nrows   #excel表格中的行数

        self.ncols = self.table.ncols #excel表格中的列数

    def read_excel(self, row):
        """读取excel表格内的文件并且使用字典表进行储存"""
        list = []
        for r in range(row, self.nrows):
            app = {}
            for col in range(self.ncols):
                value = self.table.cell(r, col).value
                ctype = self.table.cell(r, col).ctype
                if ctype == 0:
                    value = ""
                elif ctype == 1:
                    value = value
                elif ctype == 2:
                    value = int(value)
                elif ctype == 3:
                    date = datetime(*xldate_as_tuple(value, 0))
                    value = date.strftime("%Y/%m/%d  %H:%M:%S")
                elif ctype == 4:
                    if value == 0:
                        value = False
                    if value == 1:
                        value = True
                elif ctype == 5:
                    value = "错误~~~~~"
                app[self.table.cell(row-1, col).value] = value
            list.append(app)

        return list
    def write_excel(self,datas,row = 1):
        """写入excel表格"""
        new_excel = copy(self.workbook)
        ws = new_excel.get_sheet(0)
        if len(datas) == 0:
            print("错误！！！！")
        else:
            for col in range(self.ncols):
                print(datas[col], "datas[col]")
                if datas[col] != "" or datas[col] == None:
                    ws.write(row, col, datas[col])
            new_excel.save(DATAPATH+
                r"\{}.xls".format(
                    self.filename))
    def write_excel_rol(self,col,row, data):
        new_excel = copy(self.workbook)
        ws = new_excel.get_sheet(0)
        #print('写入中')
        ws.write(col, row, data)
        ws.col(0).width = 5555
        ws.col(1).width = 5555
        ws.col(2).width = 5555
        ws.col(4).width = 5555
        ws.col(5).width = 5555
        ws.col(6).width = 5555
        ws.col(8).width = 5555
        ws.col(9).width = 5555
        ws.col(10).width = 5555
        new_excel.save(DATAPATH +
                       r"/{}.xls".format(
                           self.filename))