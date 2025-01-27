#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    '''A sophisticated Rectangle class with multiple features'''

    def __init__(self, width=0, height=0):
        '''Initialize a new Rectangle instance'''
        self.width = width
        self.height = height

    def area(self):
        '''Calculate and return the rectangle's area'''
        return self.width * self.height

    def perimeter(self):
        '''Calculate and return the rectangle's perimeter'''
        return 2 * (self.width + self.height)

    def is_square(self):
        '''Check if the rectangle is a square'''
        return self.width == self.height

    def __str__(self):
        '''Return a string representation of the Rectangle'''
        return f"Rectangle(width={self.width}, height={self.height})"

    def __repr__(self):
        '''Return a formal representation of the Rectangle'''
        return f"Rectangle({self.width}, {self.height})"

    def scale(self, factor):
        '''Scale the rectangle's dimensions by a given factor'''
        self.width *= factor
        self.height *= factor
