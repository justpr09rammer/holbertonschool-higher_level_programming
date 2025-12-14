#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    This function takes any Python object and converts it into a JSON string 
    using the `json.dumps()` method. The resulting string is a representation 
    of the object in JSON format.

    Args:
        my_obj (any): The Python object to be converted into a JSON string.

    Returns:
        str: The JSON string representation of the object.

    Example:
        my_dict = {'name': 'John', 'age': 25}
        json_str = to_json_string(my_dict)
        print(json_str)  # Output: '{"name": "John", "age": 25}'
    """
    return json.dumps(my_obj)

