# -*- coding: utf-8 -*-
__author__ = 'Vitalii Turovets'

# Traditional "for loop" way
a = list()
for x in xrange(0, 10):
    if x % 2:
        a.append(x * 2)
print a

# "lambda" way
print map(lambda x: x * 2, filter(lambda x: x % 2, xrange(0, 10)))

# List comprehension way:
print [x * 2 for x in xrange(0, 10) if x % 2]

"""
Script output:
[2, 6, 10, 14, 18]
[2, 6, 10, 14, 18]
[2, 6, 10, 14, 18]
"""