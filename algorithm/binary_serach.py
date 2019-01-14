import math


# 二分查找某个数 在元组的位置
# 2 45 34 2 51 5 6  34 45 342 797


def binary_serach(data, num):
    low = 0
    high = len(data) - 1
    while low < high:
        mid = math.floor((low + high) / 2)
        if num == data[mid]:
            return mid
        elif num < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return 0


data = (12, 779, 2, 45, 34, 2, 51, 5, 6, 34, 45, 342, 797)
listData=list(data)
listData.sort()
print(listData)

resNum = binary_serach(listData, 6)
print(resNum)
