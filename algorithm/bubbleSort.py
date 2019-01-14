# 冒泡排序

def bubbleSort(list):
    count = len(list)
    for i in range(1, count):
        for j in range(0, count - i):
            # print(list[j] , list[j + 1])
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


list = [4, 21, 41, 2, 53, 1, 213, 31, 21, 423]
sortList = bubbleSort(list)
print(sortList)
