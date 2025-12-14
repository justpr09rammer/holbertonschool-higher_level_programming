#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    This class validates the width and height using the integer_validator method from BaseGeometry.
    It then initializes the width and height as private attributes.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new Rectangle instance.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates both width and height using the integer_validator method from BaseGeometry.
        If any of the values are invalid (non-integer or less than 0), a ValueError will be raised.
        """
        # Validate width and height using the integer_validator method from the BaseGeometry class
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Set the private attributes for width and height
        self.__width = width
        self.__height = height

