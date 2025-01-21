#!/usr/bin/python3
"""
This module contains a function that prints a user's full name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the user's first and last name.

    Args:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user (optional).
        
    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Validate that first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Validate that last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Use f-string for formatting the output
    full_name = f"My name is {first_name} {last_name}".strip()
    
    # Print the full name
    print(full_name)
