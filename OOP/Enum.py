# 枚举

from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

for name, member in Month.__members__.items():
  print('name: %s, member: %s' % (name, member))

# @unique 保证没有重复值
@unique
class Week(Enum):
  Sun = 0 # Sun的value被设定为0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6

print(Week.Sun)               # => Week.Sun
print(Week.Sun.value)         # => 0
print(Week(6))                # => Week.Sat
print(Week(6) == Week.Sat)    # => True
