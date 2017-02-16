#!/usr/bin/env python3
# _*_ encoding=utf-8 _*_

from io import StringIO, BytesIO

# 内存IO，1. 字符IO；2.二进制IO。

# StringIO
f = StringIO()
f.write('Hello Jack!')
content = f.getvalue()
print('content:', content)

f = StringIO('Python')
s = f.readline()
print('s:', s)

# BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
content = f.getvalue()
print(content)

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
s = f.readline()
print(s.decode('utf-8'))
