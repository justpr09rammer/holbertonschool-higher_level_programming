#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.

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
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height

        # Set the private attributes for width and height
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation in the format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

