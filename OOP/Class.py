# 定义一个 Class

# 定义一个 Student 类，同时此类继承自 Object
class Student(object):
  """docstring for Student"""
  # __init__ 为构造方法
  # self 指向类自身
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def print_score(self):
    print('name: %s, score: %s' % (self.name, self.score))

  def get_grade(self):
    x = self.score
    if x >= 90:
      return 'A'
    elif x >= 60:
      return 'B'
    else:
      return 'C'


# 使用 classname() 形式创建类实例
s = Student('Jack', 59)
print(s.name)
print(s.score)

s.print_score()
print(s.get_grade())
print(s.name)