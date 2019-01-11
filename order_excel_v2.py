import xlrd  # 导入xlrd


class ExcelData():

    def __init__(self, data_path, sheetname):
        self.data_path = data_path  # excle表格路径，需传入绝对路径
        self.sheetname = sheetname  # excle表格内sheet名
        self.data = xlrd.open_workbook(self.data_path)  # 打开excel表格
        self.table = self.data.sheet_by_name(self.sheetname)  # 切换到相应sheet
        self.keys = self.table.row_values(0)  # 第一行作为key值
        self.rowNum = self.table.nrows  # 获取表格行数
        self.colNum = self.table.ncols  # 获取表格列数

    def readExcel(self):

        mysql_str = [];
        head_str = "insert into test (client,girard,color,size,num,price) values "
        if self.rowNum < 2:
            return 'error excle 数据行数小于2!'
        else:
            for i in range(1, self.rowNum):  # 从第二行（数据行）开始取数据

                mysql_str.append("('" + self.table.row_values(i)[0] + "','" + self.table.row_values(i)[2] + "','" \
                                 + self.table.row_values(i)[3] + "','" + self.table.row_values(i)[4] + "','" \
                                 + str(self.table.row_values(i)[5]) + "','" + str(self.table.row_values(i)[6]) + "'),")

            new_mysql_str = head_str + ''.join(mysql_str)
        with open('./clientOrderV2.sql', 'w') as fileobject:  # 使用‘w’的方式打开
            fileobject.write(new_mysql_str.strip(','))  # 去掉末尾的,

        return 'successful exec end !'


if __name__ == '__main__':
    data_path = "./meetingOrder.xlsx"  # 文件的绝对路径
    sheetname = "客户订单"
    get_data = ExcelData(data_path, sheetname)  # 定义get_data对象
    result = get_data.readExcel()
    print(result)
