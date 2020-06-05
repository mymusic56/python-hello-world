# !/usr/bin/python3
# -*- coding: UTF-8 -*-

names = ["z", "b", "c", "d"]

a = ["idx:" + name for name in names]
b = {"idx:" + name: "1" for name in names}

print(a, b)

d_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = [i if i % 2 == 0 else -i for i in d_list]
print(c)
c = [i for i in d_list if i % 2 == 0]
print(c)

text = ' Today,  is, Sunday'
text_list = [item.strip() for item in text.split(',') if len(item.strip()) > 3]
print(text_list)

attributes = ['name', 'birthday', 'gender', 'address']
values = [
    ['jason', '2000-01-01', 'male'],
    ['mike', '1999-01-01', 'male', '北京市'],
    ['nancy', '2001-02-01', 'female']
]

ss = []
attr_len = len(attributes)
for value in values:
    tmp = {}
    for val in value:
        idx = value.index(val)
        if idx < attr_len:
            tmp[attributes[idx]] = val
    ss.append(tmp)
print(ss)

ss2 = [{attributes[i] : value[i] for i in range(0, len(attributes)) if i < len(value)} for value in values]
print(ss2)
