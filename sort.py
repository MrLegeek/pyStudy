# 一 list 列表
# list = [1, 6, 3, 4, 5, 2]

# 正逆序

# list.sort()  # 逆序
# print(list)
# sorted(list)  # sort是永久的，而sorted是临时的。
# print(list)
#
# list.sort(reverse=True)  # 逆序
# sorted(list, reverse=True)
# print(list)

# 反转
# reversed(list) # 反转1
# print(list)

# list[::1] # 反转2 切片方式
# print(list)

# list = [('b', 1), ('a', 1), ('c', 3), ('d', 4)]
# list.sort(key=lambda x: (x[1], x[0]))  # 对列表的第二个元素排序后，再对第一个元素排序
# print(list)


# 二 tuple 元组 先转成列表 再排序
# tuple = (1, 6, 3, 4, 5, 2)
# list=list(tuple)
# list.sort()
# print(list)


# 三 字典
# 通过key排序
# dict = {'a': 2, 'A': 1, 'c': 3, 'b': 2}
#
# sorted_key_list = sorted(dict)  # 正向排序
# # sorted_key_list = sorted(dict,reverse=True)           #逆向排序
# print(sorted_key_list)
# sorted_dict = list(map(lambda x: {x: dict[x]}, sorted_key_list))
# print(sorted_dict)

# 通过value排序
dict = {'a': 2, 'A': 1, 'c': 3, 'b': -2}
sorted_key_list = sorted(dict, key=lambda x: dict[x])  # 正向排序
# sorted_key_list = sorted(d, key=lambda x:dict[x], reverse=True)      #逆向排序
print(sorted_key_list)

sorted_dict = list(map(lambda x: {x: dict[x]}, sorted_key_list))
print(sorted_dict)

