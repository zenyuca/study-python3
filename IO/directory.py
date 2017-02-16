#!/usr/bin/env python3
# _*_ encoding=utf-8 _*_

import os

# posix: Linux, Unix, Mac OS x
# nt: Windows
print(os.name)

# environ: 获取系统环境变量
# 获取某一节点，使用 get('nodename')，如：os.environ.get('PATH')
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 拼接路径
filepath = os.path.join('/tmp', 'test')
# 创建目录
os.mkdir(filepath)
# 删除目录
os.rmdir(filepath)

value = os.path.split('./README.md')
print(value)

# 列出当前目录中所有的python文件
pyfiles = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.splitext(f)[1] == '.py']
print(pyfiles)
