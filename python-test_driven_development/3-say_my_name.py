#!/usr/bin/python3
"""
This module provides a function to print a user's full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string with the first and last name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.
        
    Raises:
        TypeError: If first_name or last_name isn't a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Use f-string for formatting the output
    full_name = f"My name is {first_name} {last_name}"
    
    # Print the full name, stripping any trailing spaces
    print(full_name.strip())
