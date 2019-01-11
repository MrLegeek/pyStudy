import csv

# 把数据写入csv中
dataRaws = [
    ['姓名', '年龄', '手机号'],
    ['张三', '23', '18934343434'],
    ['李四', '34', '18944353545'],
    ['王二', '44', '18734343443'],
    ['麻子', '12', '15742343434'],
    ['哈哈', '23', '15237839434']
]

with open('./exportToCsv.csv', 'w', encoding='utf-8', newline='')as f:
    writerCsv = csv.writer(f)
    for row in dataRaws:
        writerCsv.writerow(row)
