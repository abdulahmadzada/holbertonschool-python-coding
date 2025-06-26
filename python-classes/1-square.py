#!/usr/bin/python3
"""
This module defines a class Square.

It represents a square with optional size and value validation.
"""


class Square:
    """
    This class represents a square with a private size attribute.
    Size must be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with size validation.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
