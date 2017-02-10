# 实例属性与类属性

class Student(object):
  name = 'Student'
  def __init__(self, name):
    self.name = name

print(Student.name)     # => Student
s = Student('jack')
print(Student.name)     # => Student
print(s.name)           # => jack

s.name = 'Bruce'
print(Student.name)     # => Student
print(s.name)           # => Bruce
