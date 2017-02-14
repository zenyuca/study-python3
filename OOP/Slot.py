# solt 插槽，限制类的属性
class Student(object):
    __slots__ = ('name', 'age', 'run')

s = Student()
s.name = 'Jack'
s.age = 29
# score 没有定义在 Student 的限制属性中
# s.score = 99    # => AttributeError: 'Student' object has no attribute
# 'score'

# 定义一个外部方法


def run(self):
    print('%s is running!' % self.name)
# 将外部方法绑定到实例中
s.run = run
s.run(s)


def eat(self):
    print('%s is eating!' % self.name)
# eat 属性没有 Student 类被允许定义
# s.eat = eat     # => AttributeError: 'Student' object has no attribute 'eat'
# s.eat()
