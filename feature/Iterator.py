from collections import Iterable, Iterator
# 迭代器，不光可以迭代 List 和 Tuple，也可以迭代 Dict 和 字符串

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

# 迭代 Dict
d = {
    'a': 1,
    'b': 2,
    'c': 3
}

# 打印结果：
# b
# c
# a
for key in d:
    print(key)

# 打印结果：
# 2
# 3
# 1
for key in d:
    print(d[key])

# 使用 enumerate 获取迭代的下标

# index: 0, key: c
# index: 1, key: a
# index: 2, key: b
for i, key in enumerate(d):
    print('index: %d, key: %s' % (i, key))

# 打印结果：
# a
# b
# c
# d
s = 'abcd'
for ch in s:
    print(ch)

# 使用 enumerate 获取迭代的下标

# index: 0, ch: a
# index: 1, ch: b
# index: 2, ch: c
# index: 3, ch: d
for i, ch in enumerate(s):
    print('index: %d, ch: %s' % (i, ch))


# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
print(isinstance('abc', Iterable))      # => True
print(isinstance([1, 2, 3], Iterable))  # => True
print(isinstance({'a': 1}, Iterable))    # => True

# 同时引用两个变量，遍历二维数组
for x, y in [[1, 2], [3, 4], [5, 6]]:
    print(x, y)

for x, y in [(1, 2), [3, 4], [5, 6]]:
    print(x, y)


def g():
    yield 1
    yield 2
    yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

d = {'a': 1, 'b': 2, 'c': 3}

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)
