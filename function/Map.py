# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f (x):
  return x ** 2

l = [1, 2, 3, 4]
r = map(f, l)     # 返回一个 Iterable
print(list(r))    # => [1, 4, 9, 16] 将 Iterator 转换成 List

suffix = '00'
def f (ch):
  return ch + suffix

l = 'abcde'
r = map(f, l)
# print(list(r))

from collections import Iterator, Iterable
print(isinstance(l, Iterator))    # => False
print(isinstance(l, Iterable))    # => True

print(type(r))

s = ''
for item in r:
  s += item

print(s)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def fn (x, y):
  return x * 10 + y

def char2num (s):
  return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

s = reduce(fn, map(char2num, '134687'))
print()
print('Type:',type(s),'\tValue:',s)

s = 'you are beautiful girl'
flag = True
result = ''
for i, ch in enumerate(s):
  if flag:
    result += ch.upper()
    flag = False
    continue
  if ch == ' ':
    flag = True
  result += ch

print(result)

def normalize (name):
  s = ''
  for i, ch in enumerate(name):
    if i == 0:
      s += ch.upper()
    else:
      s += ch.lower()
  return s

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
