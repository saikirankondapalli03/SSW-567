'''
@author Sai
File name: HW-01.py
Date created: 1/28/2020
Date last modified: 1/28/2020
Python Version: 3.1
This program takes measurements of 3 sides and displays whether it is
a) Isosceles  b) Equilateral c) Right Triangle d) Scalene
'''

from numbers import Number

def classify_triangle(a, b, c):
    '''
    this function takes 3 sides as input.validates all 3 sides and check if it is triangle or not.
    '''
    if not isinstance(a, Number) or not isinstance(b, Number) or not isinstance(c, Number):
        return 'invalid input'
    if a<=0 | b<=0 | c<=0:
        return 'invalid input'
    if a + b <= c or b + a <= c or a + c <= b:
        return 'invalid input'
    if a == b and a == c:
        return 'Equilateral triangle'
    if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        return 'Isoceles triangle'
    if  a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return 'Right angled triangle'
    if  a!=b and b!=c  and c!=a:
        return 'Scalene triangle'

import unittest 
class TestCases(unittest.TestCase):
    """This is a testing class for the classify_triangles method"""
    def test_equilateral_triangle(self):
        assert classify_triangle(1, 1, 1) == 'Equilateral triangle'
        assert classify_triangle(100, 100, 100) == 'Equilateral triangle'
        assert classify_triangle(0, 0, 0) != 'Equilateral triangle'

    def test_right_angled_triangle(self):
        """Test that right triangles are identified"""
        assert classify_triangle(15,17,8) == 'Right angled triangle'
        assert classify_triangle(28,45,53) == 'Right angled triangle'
        assert classify_triangle(12,5, 13) == 'Right angled triangle'
    
    def test_isoceles_triangle(self):
        assert classify_triangle(10, 10, 10) != 'Isoceles triangle'
        assert classify_triangle(5, 5, 3) == 'Isoceles triangle'

    def test_Scalene_triangle(self):
        assert classify_triangle(13, 9, 14) == 'Scalene triangle'
        assert classify_triangle(7.7, 5, 9) == 'Scalene triangle'
    
    def test_invalid_triangle(self):
        assert classify_triangle(-1, -1, -9) == 'invalid input'
        assert classify_triangle(0, 0, 0) == 'invalid input'


if __name__ == '__main__':
    # note: there is no main(). Only test cases here
    unittest.main(exit=False, verbosity=2)