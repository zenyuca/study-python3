# @property 将类的方法变成属性调用


class Student(object):

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError('name 应该是一个 String')

    # hello 属性为只读
    @property
    def hello(self):
        print('Hello %s! Welcome to Python world!' % self.__name)

s = Student()
s.name = 'Jack'       # 像属性调用一样的调用设置方法
name = s.name         # 像获取属性一样地调用获取方法
print(name)
# hello 看起来像是一个属性，背后绑定的却是一个方法
s.Hello               # => Hello Jack! Welcome to Python world!
