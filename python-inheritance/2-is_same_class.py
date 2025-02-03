#!/usr/bin/python3
'''Module for is_same_class method'''

def is_same_class(obj, a_class):
    '''Check if an object is exactly an instance of a given class.

    Args:
        obj (object): The object to check.
        a_class (class): The class

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    '''
    return type(obj) is a_class

if __name__ == "__main__":

    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
