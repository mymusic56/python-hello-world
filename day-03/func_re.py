# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)

# match尝试从起始位置找到匹配的字符串
m = pattern.match('Hello World Wide Web')

print(m.groups())

rs = re.compile(r'\d+').match('one12twothree34four')
print(rs)
rs = re.compile(r'\d+').match('one12twothree34four', 3)
print(rs)
rs = re.compile(r'\d+').findall('one12twothree34four')
print(rs)
rs = re.compile(r'\d+').finditer('one12twothree34four')
for match in rs:
    a = match.group()
    print(type(a),a)

