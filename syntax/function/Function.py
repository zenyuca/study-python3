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

# 对参数进行检查
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

# 函数返回多值
import math

def move (x, y, step, angle = 0):
  nx = x + step * math.cos(angle)
  ny = y + step * math.sin(angle)
  return nx, ny

x, y = move(0, 0, 60, math.pi / 3)
print(x, y)
