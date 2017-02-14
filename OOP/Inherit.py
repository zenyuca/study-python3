# 继承


class Animal(object):

    def running(self):
        print('动物在奔跑……')


class Dog(Animal):
    pass


class Cat(Animal):
    pass

d = Dog()
# Dog 继承的父类 Animal 的 running 方法
d.running()     # => 动物在奔跑……

c = Cat()
d.running()     # => 动物在奔跑……


class Dog(Animal):
    # 子类重写父类的同名方法

    def running(self):
        # super() 为父类的引用
        super().running()
        print('狗狗在奔跑……')


d = Dog()
d.running()     # => 狗狗在奔跑……

print('Dog == Animal,\t', isinstance(d, Animal))     # => Dog == Animal, True
print('Cat == Animal,\t', isinstance(c, Animal))     # => Cat == Animal, True
print('Dog == Cat,\t\t\t', isinstance(d, Cat))       # => Dog == Cat,    False
