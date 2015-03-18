# -*- coding: utf-8 -*-
__author__ = 'Vitalii Turovets'


class ExampleDict():
    def __init__(self):
        self.dict = dict({
            'username': "username",
            'password': "password",
            'host': "localhost",
            'port': 1234
        })

    def __getitem__(self, item):
        return self.dict[item]

    def __call__(self):
        return self.dict


class ExampleIterable():
    def __init__(self, lst):
        self.lst = lst
        self.index = -1

    def __iter__(self):
        return self

    def next(self):
        if self.index < len(self.lst) - 1:
            self.index += 1
            return self.lst[self.index]
        else:
            raise StopIteration


if __name__ == '__main__':
    example_dict = ExampleDict()

    print "Dict:\n" \
          "Username: %(username)s\n" \
          "Password: %(password)s\n" \
          "Host: %(host)s\n" \
          "Port: %(port)s\n" % example_dict

    example_iterable = ExampleIterable(xrange(0, 6))
    print "Iteration:"
    for x in example_iterable:
        print x

"""
Script output:
Dict:
Username: username
Password: password
Host: localhost
Port: 1234

Iteration:
0
1
2
3
4
5
"""