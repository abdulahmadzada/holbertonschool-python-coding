#!/usr/bin/python3
"""
This module defines a class Square that represents a square.
"""


class Square:
    """
    This class represents a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of one side of the square (no type/value check).
        """
        self.__size = size
