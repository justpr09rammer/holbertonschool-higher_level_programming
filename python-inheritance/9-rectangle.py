#!/usr/bin/python3
"""
Module for defining a Rectangle class that inherits from BaseGeometry.

This module contains the `Rectangle` class, which inherits from the `BaseGeometry` class.
It includes methods to validate the rectangle's dimensions, calculate its area, and provide
a string representation of the rectangle in the format [Rectangle] <width>/<height>.

The `Rectangle` class validates that the `width` and `height` are positive integers using the
`integer_validator` method inherited from `BaseGeometry`.

Functions:
    Rectangle: A class that represents a rectangle, with methods to validate its dimensions,
               compute its area, and provide a string representation.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.

    This class inherits from BaseGeometry and validates that the dimensions (width and height) 
    are positive integers before assigning them to private attributes. It also provides methods
    for calculating the area of the rectangle and returning its string representation.

    Attributes:
        __width (int): The width of the rectangle, validated as a positive integer.
        __height (int): The height of the rectangle, validated as a positive integer.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle object with width and height.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle in the format [Rectangle] <width>/<height>.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates the width and height using the integer_validator method from BaseGeometry.
        
        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If the width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height

        # Set the private attributes for width and height
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        The area is calculated by multiplying the width and height of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        The string representation is in the format:
        [Rectangle] <width>/<height>

        Returns:
            str: The string representation in the format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

