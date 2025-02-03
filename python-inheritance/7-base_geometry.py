#!/usr/bin/python3
"""This module contains a BaseGeometry"""


class BaseGeometry:
    """This class represents a base geometry."""

    def area(self):
        """
        This method raises an exception.

        Raises:
            Exception: Always raises an exception with the message
                       'area() is not implemented'
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        This method validates the value.

        Args:
            name (str): The name of the value being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
