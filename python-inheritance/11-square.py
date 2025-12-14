#!/usr/bin/python3
"""
Module for creating a Square class that inherits from Rectangle.

This module contains a `Square` class which inherits from `Rectangle`. The `Square`
class has specific behavior for the square's size and its area calculation, while
still utilizing the `integer_validator` method for validating the size. The class
also overrides the `__str__` method to print the description of the square.

Functions:
    Square: A class that represents a square, inheriting from Rectangle.
"""

from 9-rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square, validated as a positive integer.

    Methods:
        __init__(self, size): Initializes a new Square object with size.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the square in the format [Square] <size>/<size>.
    """

    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
        
        Validates the size using the integer_validator method from Rectangle.
        The size is set for both the width and height (since it’s a square).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)  # Call the parent class constructor with the same size for width and height

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"

