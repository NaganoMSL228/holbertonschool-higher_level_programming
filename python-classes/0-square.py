#!/usr/bin/python3
"""
This module defines a Car class that represents a car object,
with attributes for make and model.
"""


class Car:
    """
    A class that represents a car.

    Attributes:
        make (str): The make of the car.
        model (str): The model of the car.
    """

    def __init__(self, make, model):
        """
        Initializes a new Car instance with the specified make and model.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
        """
        self.make = make  # Public attribute
        self.model = model  # Public attribute

# Example of creating an instance of the Car class


if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla")
    print(f"My car is a {my_car.make} {my_car.model}.")
    print(my_car.__dict__)  # Displaying the attributes of the instance
