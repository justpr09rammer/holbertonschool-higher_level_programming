#!/usr/bin/python3
"""Module defining the MyList class that inherits from list."""

class MyList(list):
    """A class that inherits from list and adds a method to print sorted list."""

    def print_sorted(self):
        """
        Prints the list in ascending order.

        This method does not modify the original list, it only prints the sorted list.
        """
        print(sorted(self))

