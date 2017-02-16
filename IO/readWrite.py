#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

try:
    # 读取（ r 选项） README.md 文件
    f = open('./README.md', 'r')
    # 读取所有内容
    content = f.read()
    print(content)
finally:
    if f:
        # 关闭文件流管道
        f.close()

# with 写法自动调用 close 方法，等价于上面
with open('./README.md', 'r') as f:
    content = f.read()
    print(content)

with open('./readWrite.py', 'r') as f:
    # 一行一行地读取文件内容，适合配置文件文件读取。
    for line in f.readlines():
        print(line)

# 读取二进制文件 open('filename', 'rb')
# 指定编码集读取，open('filename', 'r', encoding='gbk')


# 向指定文件写入数据，如果文件不存在，则自动创建此文件。
f = open('./test.txt', 'w')
d = {
    'name': 'jack',
    'age': 19,
    'score': 90
}
f.write(json.dumps(d))
f.close()

with open('./test.txt', 'w') as f:
    f.write(json.dumps(d))
