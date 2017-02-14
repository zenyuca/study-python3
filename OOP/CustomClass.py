# 定制类


class Student(object):
    # 限制类实例可以允许属性值
    __slots__ = ('__name', '__age', '__index', '__subject')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__subject = ['语文', '数学', '英语']
        self.__index = 0

    # 通过装饰器 @property 将方法的改装成的属性调用，
    # 不能在 __slots__ 元组中定义
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    # 1. __str__ 类似 java 中的 toString
    def __str__(self):
        return 'Student object:(%s, %s)' % (self.name, self.age)

    # 让 len 方法可以作用于实例对象
    def __len__(self):
        return len(self.__str__())

    # 返回一个 iterator ，在 for in 对象时，循环调用 iterator 的 __next__ 方法，
    # 本例迭代器（iterator）就是自身
    def __iter__(self):
        # return iter([1, 2, 3])
        return self
    # __next__ 方法为迭代器所必有

    def __next__(self):
        if self.__index == len(self.__subject):
            raise StopIteration()
        value = self.__subject[self.__index]
        self.__index = self.__index + 1
        return value

    # 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
    # 最后，还有一个__delitem__()方法，用于删除某个元素。
    # 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
    # 这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

    # 像根据下标一样取出迭代器的某个值
    # 如：
    # s = Student()
    # s[0]
    def __getitem__(self, n):
        return self.__subject[n]

    # 获取类中未定义的属性
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    # 将实例的引用改造成像方法一样的调用
    # def __call__(self):
    #     return 'Student name is %s' % self.name

    def __call__(self, age):
        return 'Student name is %s, it\'s age is %s' % (self.name, self.age)


s = Student('Jack', 20)
print(s.name)           # => Jack
s.name = 'Bruce'
print(s.name)           # => Bruce

# 打印一个类实例，默认先调用 __str__ 方法，
# 如果本类未定义 __str__ 方法，那么调用父类的  __str__ 方法，
# 如果还没有，找到 object 类的  __str__ 方法
print(s)                # => Student object:(Bruce, 20)

# 调用实例的 __len__ 方法
print(len(s))

# 语文
# 数学
# 英语
for item in s:
    print(item)

print(s[0])       # => 语文

print(s.score)

# 实例引用变成了一个函数
print(s(12))      # => Student name is Bruce, it's age is 20
# callable 函数检查变量是否是函数
print('s is funtion = ', callable(s))            # => s is funtion =  True
# => Number is function =  False
print('Number is function = ', callable(2))
print('max is function = ', callable(max))       # => max is function =  True
