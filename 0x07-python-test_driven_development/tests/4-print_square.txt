>>> print_square = __import__('4-print_square').print_square

>>> print_square(4)
####
####
####
####
>>> print_square(0)

>>> print_square(1)
#
>>> print_square(-1)
Traceback (most recent call last):
    ...
ValueError: size must be >= 0

>>> print_square("string")
Traceback (most recent call last):
    ...
TypeError: size must be an integer

>>> print_square(None)
Traceback (most recent call last):
    ...
TypeError: size must be an integer

>>> print_square(True)
#

>>> print_square(-1.0)
Traceback (most recent call last):
    ...
TypeError: size must be an integer
