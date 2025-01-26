#!/usr/bin/python3
'''Test script for the Square class.'''

Square = __import__('4-square').Square

# Create an instance of Square with an initial size
my_square = Square(89)
print(f"Area: {my_square.area()} for size: {my_square.size}")

# Modify the size of the square
my_square.size = 3
print(f"Area: {my_square.area()} for size: {my_square.size}")

# Attempt to modify the size with an invalid value
try:
    my_square.size = "5 feet"  # Invalid value to test error handling
    print(f"Area: {my_square.area()} for size: {my_square.size}")
except TypeError as te:
    print(te)  # Print the error message for TypeError
except ValueError as ve:
    print(ve)  # Print the error message for ValueError
except Exception as e:
    print(f"An unexpected error occurred: {e}")  # Handle other exceptions

# Final display of area and size
print(f"Final Area: {my_square.area()} for final size: {my_square.size}")
