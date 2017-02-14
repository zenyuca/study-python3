# Generator 生成器。列表生成器产生的数组会存在于内存中，
# 如果只使用部分数据，势必是一种浪费。
# 在 Python 中，有一种一边计算一边循环的机制，叫做生成器（generator）

# 创建一个生成器，只需像列表生成器一样，只是把 [] 改成 ()
l = [x for x in range(10)]
print(l)            # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  可以直接打印出值
print(type(l))      # => <class 'list'>

g = (x for x in range(10))
print(g)            # => <generator object <genexpr> at 0x7f04e7d5b3b8>   不能直接打印出其值
print(type(g))      # => <class 'generator'>

# 通过 next 函数边循环边获取值
print(next(g))      # => 0
print(next(g))      # => 1
print('')

# 1 1 2 3 5 8 13


def fib(max):
    l = []
    n, a, b = 0, 0, 1
    while n < max:
        l.append(b)
        a, b = b, a + b
        n = n + 1
    return l

print(fib(10))

# 注意，赋值语句：
# a, b = b, a + b

# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

# 自定义一个生成器


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(9)
# 只要一个函数里面包含 yield ，那么这就是一个 generator
print('type(g):', type(g))    # => type(g): <class 'generator'>
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)

l = zip('abcd', [1, 2, 3, 4], {'a': 1, 'b': 2, 'c': 3})
print(list(l))


def triangles():
    l = [1]
    while True:
        yield l
        l = [1] + [x + y for x, y in zip(l[1:], l[:-1])] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 15:
        break
