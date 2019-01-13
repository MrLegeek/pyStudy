import xlwt

book = xlwt.Workbook(encoding='utf-8')

sheet = book.add_sheet('Sheet1')

rowData = {
    '0': ['姓名', '语文', '数学', '英语'],
    '1': ['张三', '90', '134', '120'],
    '2': ['李四', '78', '45', '23'],
    '3': ['王二', '99', '23', '89'],
    '4': ['麻子', '45', '77', '93'],
    '5': ['哈哈', '63', '110', '101'],
};

for line in rowData:

    for r in range(0, len(rowData[line])):
        # print(line, r, rowData[line][r])
        sheet.write(int(line), r, rowData[line][r])

# 保存Excel book.save('path/文件名称.xls')
book.save('simple.xls')
