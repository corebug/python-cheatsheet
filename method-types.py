# -*- coding: utf-8 -*-
__author__ = 'Vitalii Turovets'


class MyClass():
    def test_method(self):
        return "Ok, normal method"

    @classmethod
    def test_classmethod(cls):
        return "Ok, classmethod"

    @staticmethod
    def test_staticmethod():
        return "Ok, staticmethod"

my_object = MyClass()
print MyClass.test_classmethod()
print MyClass.test_staticmethod()
print my_object.test_method()
print my_object.test_classmethod()
print my_object.test_staticmethod()

"""
Script output:
Ok, classmethod
Ok, staticmethod
Ok, normal method
Ok, classmethod
Ok, staticmethod
"""