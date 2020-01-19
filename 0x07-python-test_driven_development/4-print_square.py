#!/usr/bin/python3
"""
This is the print_square module.
The print_square module provides a simple function print_square()
that prints a square with #.
"""


def print_square(size):
    """Print square with #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
