# 使用循环实现输出2-3+4-5+6.....+100的和
#
# sum = 0
#
# for i in range(2, 101):
#
#     if i % 2 == 0:
#         sum += i
#     else:
#         sum -= i
#
# print(sum)


# 写代码，有如下变量，请按照要求实现每个功能
#
name = " aleX "
# a.移除name变量对应的值两边的空格，并输入移除有的内容

# print(name.strip())

# b.判断name变量对应的值是否以 "al"开头，并输出结果

# res=name.startswith('al')
# print(res)

# c.判断name变量对应的值是否以 "X"结尾，并输出结果

# res=name.endswith('X')
# print(res)

# d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果

# res=name.replace('l','p')
# print(res)

# e.将name变量对应的值根据 " l" 分割，并输出结果。

# res=name.split('l')
# print(res)

# f.请问，上一题 e分割之后得到值是什么类型？

# re=type(name.split('l'))
# print(re)

# g.将name变量对应的值变大写，并输出结果

# res=name.upper()
# print(res)

# h.将name变量对应的值变小写，并输出结果

# res=name.lower()
# print(res)

# i.请输出name变量对应的值的第2个字符？

# res=name[1]
# print(res)

# j.请输出name变量对应的值的前3个字符？

# res=name[2]
# print(res)

# k.请输出name变量对应的值的后2个字符？

# res=name[-2:]
# print(res)

# l.请输出name变量对应的值中 "e" 所在索引位置？

res=name.find('e')
# res=name.index('e')
print(res)