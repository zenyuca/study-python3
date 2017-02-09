# filter Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 性质：过滤函数
# 功能：针对偶数
def is_odd (n):
  return n % 2 == 0

ls = [1, 2, 3, 4, 5, 6]
ls = filter(is_odd, ls)     # True 保留, False 丢弃
print(type(ls))             # <class 'filter'>
ls = list(ls)               # 将 filter 转换成 list
print(ls)                   # [2, 4, 6]

def not_empty (s):
  # 值先为真（除 None、0、''、False），再前后去除空格
  return s and s.strip()

ls = ['abc', None, '', 'DD', '  ', ' a b ']
print(list(filter(not_empty, ls)))        # ['abc', 'DD']

b = '   '.strip()
print(b)              # 空串值 ，递归去除了多个空格

s = ' a b a '
print(s.strip())      # => a b a 前后去空格
print(s.strip(' a'))  # => b 递归前后去除指定字符

