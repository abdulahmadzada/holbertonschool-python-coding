#!/usr/bin/python3
"""
This module defines a class Square that represents a square with size validation.
"""


class Square:
    """
    This class represents a square and allows for area calculation.
    The size of the square is validated to be a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with an optional size.

        Args:
            size (int): The size of one side of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
