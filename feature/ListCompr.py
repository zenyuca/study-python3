# 列表生成器
ls = [x*x for x in range(1, 11)]
print(ls)   # => [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 迭代的同时过滤结果
ls = [x*x for x in range(1, 11) if x % 2 == 0]
print(ls)   # => [4, 16, 36, 64, 100]

# 同时迭代两组数据
ls = [x + '=' + y for x in 'ABC' for y in 'XYZ']
print(ls)   # => ['A=X', 'A=Y', 'A=Z', 'B=X', 'B=Y', 'B=Z', 'C=X', 'C=Y', 'C=Z']

import os
ls = [d for d in os.listdir()]
print(ls)

d = {
  'x': 'A',
  'y': 'B',
  'z': 'C'
}
ls = [key + ': ' + value for key, value in d.items()]
print(ls)

L = ['Hello', 'World', 18, 'Apple', None]
ls = [s.lower() for s in L if isinstance(s, str)]
print(ls)     # => ['hello', 'world', 'apple']
