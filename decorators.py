# -*- coding: utf-8 -*-
__author__ = 'Vitalii Turovets'

from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "decorator1 begin\n%s\ndecorator1 end" % str(func(*args, **kwargs))
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "decorator2 begin\n%s\ndecorator2 end" % str(func(*args, **kwargs))
    return wrapper

@decorator1
@decorator2
def original_function():
    return "Original function goes here."

if __name__ == '__main__':
    print original_function()


"""
Script output:
decorator1 begin
decorator2 begin
Original function goes here.
decorator2 end
decorator1 end
"""