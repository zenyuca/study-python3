# 定义一个函数
def my_abs(x):
  if x >= 0:
    return x
  else:
    return -x

print(my_abs(-440))   # => 440

# 定义一个空函数
# pass 占位符，可以先定义让代码先运行起来
def nop():
  pass


print(nop())      # => None

def my_abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError('错误的操作参数')
  if isinstance(x, bool):
    if x:
      return 1
    else:
      return 0
  if x >= 0:
    return x
  else:
    return -x
print(my_abs(True))
