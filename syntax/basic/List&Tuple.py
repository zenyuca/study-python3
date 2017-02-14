# list 列表（js中的数组）
ls = [1, 2, 3]
print(len(ls))    # 获得list长度

print(ls[0])      # => 1 获取下标为0的元素
print(ls[1])      # => 2 获取下标为1的元素
print(ls[-1])     # => 3 获取倒数第一个
print(ls[-3])     # => 1 获取倒数第三个

# 末尾追加元素
ls.append(4)
print(ls)         # => [1, 2, 3, 4]

# 末尾删除元素
ls.pop()
print(ls)         # => [1, 2, 3]

# 指定下标添加元素
ls.insert(0, -1)
print(ls)         # => [-1, 1, 2, 3]

# 指定下标删除元素
ls.pop(0)
print(ls)         # => [1, 2, 3]

# 指定下标替换元素
ls[0] = 0
print(ls)         # => [0, 2, 3]

# tuple 元组，类似与list，但一旦初始化即不可更改值
t = (1, 2)
print(t)
# t.insert(0, 2)    # AttributeError: 'tuple' object has no attribute 'insert'
# t.pop()           # AttributeError: 'tuple' object has no attribute 'pop'
t = (1)     # => 1 看似定义了一个长度的元组，实际上是数字1，因为小括号优先解释了
print(t)
t = (1,)    # => (1,) 正确定义了一个长度的元组，要点是在元素末尾显示注明逗号
print(t)

# 请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
