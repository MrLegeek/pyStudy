#  斐波那契数列 :0、1、1、2、3、5、8、13、21、34
def fib(n):
    if n < 0:
        return 0
    elif n <= 1 and n >= 0:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


data = fib(10)
print(data)
