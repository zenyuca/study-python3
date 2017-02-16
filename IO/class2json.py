#!/usr/bin/env python3
# _*_ encoding=utf-8 _*_
import json
from Base import Base
from io import StringIO


class Student(Base):

    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def toObject(self, d):
        return Student(d['name'], d['age'])

s = Student('Brude', 20)
s.name = 'Jack'
s.age = 19

json_str = s.toJSON()

f = StringIO(json_str)
v = f.read()

s1 = json.loads(v, object_hook=s.toObject)
print(type(s1))
print(s1.toJSON())

s2 = json.loads(v)
print(type(s2))
