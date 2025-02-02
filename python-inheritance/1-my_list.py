#!/usr/bin/python3
'''This module defines a class MyList that extends the built-in list class.'''


class MyList(list):
    '''A class that inherits from the built-in list class.'''
    
    def print_sorted(self):
        '''Prints the elements of the list in ascending order.'''
        print(sorted(self))
