#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = 2;
while (i < 100):
    j = 2;
    while (j < i):
        if not(i % j):
            break
        else:
            j += 1
    else:
        print(i, end=" ")
    i += 1
print("是素数")
print("Good by")