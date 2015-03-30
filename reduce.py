# -*- coding: utf-8 -*-
__author__ = 'Vitalii Turovets'

# Traditional way
result = 1

for num in xrange(1, 11):
    result *= num

print result

# Python's beautiful "reduce"
print reduce(lambda res, x: res * x, xrange(1, 11))


"""
Script output:
3628800
3628800
"""