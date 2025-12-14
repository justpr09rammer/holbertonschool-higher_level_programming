#!/usr/bin/python3
"""
Module for checking if an object is an instance of, or inherits from, a specified class.

This module contains a function `is_kind_of_class` that checks if an object is either 
an instance of a specific class or if the object is an instance of a class that inherits
from that specified class. This function is useful for situations where you want to check
for inheritance without worrying about exact class matching.

Functions:
    is_kind_of_class(obj, a_class): Returns True if obj is an instance of, or inherits from, a_class.
"""
def is_kind_of_class(obj, a_class):
    """Tests if an object is an instance of the specified class,
    or any class inherited from it.

    Args:
        obj (any): object of any type
        a_class (class): class to test against

    Returns:
        True if obj is instance of a_class or a subclass of a_class,
            False otherwise.

    """
    return (isinstance(obj, a_class))
