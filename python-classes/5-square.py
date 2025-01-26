#!/usr/bin/python3
'''Module for the Square class'''


class Square:
    '''A class representing a square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes the square with a given size and position.'''
        self.size = size      # Use the setter to validate size
        self.position = position  # Use the setter to validate position

    @property
    def size(self):
        '''Getter for size.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter for size with validation.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''Getter for position.'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter for position with validation.'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Returns the area of the square.'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square using the character #.'''
        if self.size == 0:
            print("")  # Print an empty line if size is 0
            return

        # Print empty lines based on position[1]
        print("\n" * self.position[1], end="")

        # Print the square with spaces based on position[0]
        for _ in rang
