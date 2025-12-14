#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object with.

    Returns:
        bool: True if the object is exactly an instance of the specified class, 
              False otherwise.
    """
    return type(obj) == a_class

