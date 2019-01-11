import csv

# 读取csv文件
with open('./readCsv.csv', 'r', encoding='utf-8')as f:
    content = csv.reader(f)
    listData = list(content)
    print(listData)
    loop = 1
    for data in listData:

        if data[0] and loop != 1:
            print(' name:' + data[0] + '-' + 'age:' + data[1] + '-' + 'phone:' + data[2] + '\n')
        loop += 1

    print(len(listData))
