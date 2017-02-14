# 定义类的私有变量


class Student(object):
    """docstring for Student"""

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    # 定义 getter 和 setter 来访问私有变量
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

stu = Student('jack', 90)

# 私有属性“__name”在解释时，被添加的前缀“_类名”，
# 所以可以通过 _Stuent__name 访问，
# 但是不同的解释器添加的前缀不一样，
# 所有不能这么做。
print(stu._Student__name)       # => jack
print(stu.get_name())           # => jack
# 当以“__”为前缀的属性，为私有属性
# 外部不能通过实例直接访问
# => AttributeError: 'Student' object has no attribute '__name'
print(stu.__name)
