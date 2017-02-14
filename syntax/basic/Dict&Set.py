# Dict（Java中的Map，JS中的对象） 和 Set

# Dict key-value
# 数字 key
d = {
    1: 'a',
    2: 'b'
}
print(d)      # => {1: 'a', 2: 'b'}
print(d[2])   # => b

# 字符串 key
d = {
    '1': 'aa',
    '2': 'bb'
}
print(d)      # => {'2': 'bb', '1': 'aa'}
print(d['1'])  # => aa
# print(d['a']) # 如果没有对应的 key 那么直接报错

# 使用 in 判断 key 是否存在
print('a' in d)   # => False
print(1 in d)     # => False

# 使用 get 函数获取 value
# 如果 value 不存在，则返回 None
print(d.get('1'))  # => aa
print(d.get(1))   # => None

if d.get(1) is None:
    print('字典 d 中不存在 key：1')

# 使用 pop 函数，根据 key 删除 value
# d.pop('dd')   # key（dd）不存在，直接报错
# d.pop('1')
print(d.pop('1'))   # => aa 删除 key 以及对应的 value，并返回 value
print(d)            # => {'2': 'bb'}

# 使用 [] 向字典中动态添加键值对，如果 key 存在覆盖其 value
d[1] = 'abc'  # 添加键值对
print(d)      # => {1: 'abc', '2': 'bb'}
d[1] = 'efg'  # 覆盖指定 key 的 value
print(d)      # => {'2': 'bb', 1: 'efg'}

# Set 无重复集合
s = set([1, 2, 3])    # 使用数组初始化一个 set
print(s)            # => {1, 2, 3}

s = set([1, 1, 2, 3])
print(s)            # => {1, 2, 3} 自动去重

s = set(list(range(10, 20)))
print(s)            # => {10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

# 使用 add 函数添加一个元素
s = set()       # 创建一个空值 set
print(s)        # => set()
print(s.add('abc'))    # => None 添加一个元素，并返回 None
print(s)        # => {'abc'}

# 使用 remove 函数删除一个元素
s = set([1, 2, 3])
s.remove(1)
print(s)        # => {2, 3}

a = 'abcd'
s = set([a, 'b', 'c'])
print(s)            # => {'c', 'abcd', 'b'}
print(s.remove(a))  # => None 删除一个指定的元素，返回 None
print(s)            # => {'b', 'c'}

# 使用 &、| 求两个 set 的交集、并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
a = s1 & s2     # 求交集
print(a)        # => {2, 3}
b = s1 | s2     # 求并集
print(b)        # => {1, 2, 3, 4}
