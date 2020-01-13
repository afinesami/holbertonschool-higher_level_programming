#!/usr/bin/python3
"""
This is the "matrix_divided" module.
"""


def matrix_divided(matrix, div):

    if div == 0:
        raise ZeroDivisionError(err_msg["ZeroDiv"])

    if not isinstance(div, (int, float)) or isinstance(div, (bool)):
        raise TypeError(err_msg["NaN"])
    if type(matrix) != list:
        raise TypeError(err_msg["Not_Matrix"])
