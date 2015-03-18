# -*- coding: utf-8 -*-
__author__ = 'Vitalii Turovets'


class Point:
    def __init__(self, x, y):
        self.coords = {'x': x, 'y': y}

    def get_coords(self):
        return self.coords


class Pixel(Point):
    def __init__(self, x, y,  brightness):
        Point.__init__(self, x, y)
        self.coords.update({'brightness': brightness})
   
if __name__ == '__main__':
    a = Point('10', '12')
    print a.get_coords()
    b = Pixel(a.coords['x'], a.coords['y'], '15')
    print b.get_coords()

"""
Script output:
{'y': '12', 'x': '10'}
{'y': '12', 'x': '10', 'brightness': '15'}
"""