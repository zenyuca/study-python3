# 偏函数

# 当函数的参数个数太多，需要简化时，
# 使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

# partial 隶属于 functools

# int(<数字串>, [进制])
# 将数字串按提供的进制转换，最终表现为 10 进制的数字
# 默认按 10 进制转换
import functools

i = int('101010', 2)
print(i)      # => 按 2 进制转换数字串

i = int('10')
print(i)      # => 10 默认按 10 进制转换数字串

i = int('20', 8)
print(i)      # => 16

i = int('f', 16)
print(i)      # => 15

i = int('11', 9)
print(i)      # => 10 将“9进制”表示的“11”转换成“10进制”形式

# 需求：提供一个函数，默认按“2进制”转换数字串
# 自定义函数


def int2(n):
    return int(n, 2)

i = int2('101010')
print(i)      # => 42

# 如上所示，自定义函数包装
# 在 Python 中提供一种固定参数方法
# functools.partial

int2 = functools.partial(int, base=2)
i = int2('101010')
print(i)      # => 42

int8 = functools.partial(int, base=8)
i = int8('10')
print(i)      # => 8
