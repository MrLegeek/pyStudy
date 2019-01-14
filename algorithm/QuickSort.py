# 快排
def QuickSort(list):
    loop = len(list)
    if loop <= 1:
        return list

    left, right = [], []
    baseNum = list[0]
    for i in range(1, loop):
        if list[i] < baseNum:
            left.append(list[i])
        else:
            right.append(list[i])

    left = QuickSort(left)
    right = QuickSort(right)

    left.append(baseNum)
    return left + right


list = [4, 21, 41, 2, 53, 1, 213, 31, 21, 423, -100]
data = QuickSort(list)
print(data)
