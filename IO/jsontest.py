#!/usr/bin/env python3
# _*_ encoding=utf-8 _*_

import json

d = dict(name='jack', age=90)
v = json.dumps(d)
print(v)

d = {
    'name': 'jack',
    'age': 10
}

v = json.dumps(d)
print(v)

json_str = '{"name": "jack", "age": 19}'
d = json.loads(json_str)
print(d)
