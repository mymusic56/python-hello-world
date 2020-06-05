# !/usr/bin/python3
# -*- coding: UTF-8 -*-


try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('IndexError Error: {}'.format(err))

print('continue')


def division(a, b):

    try:
        c = a/b
        return c
    except (ValueError, ZeroDivisionError) as err:
        # return False
        # pass
        print('Error: {}'.format(err))
    except Exception as err:
        print('Other Error: {}'.format(err))
    finally:
        print("---------------")

print(division(1, 2))