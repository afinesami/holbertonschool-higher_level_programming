Importing the function from the module:
>>> matrix_divided = __import__("2-matrix_divided").matrix_divided

Check: module docstring:
>>> m = __import__("2-matrix_divided").__doc__
>>> len(m) > 1
True

Check: function docstring:
>>> f = __import__("2-matrix_divided").matrix_divided.__doc__
>>> len(f) > 1
True

Check: passing None as matrix:
>>> matrix_divided(None, 1)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Check: passing None as div:
>>> matrix_divided([[1, 2, 3], [1, 2, 3]], None)
Traceback (most recent call last):
...
TypeError: div must be a number

Check: matrix as string:
>>> matrix_divided("Hello world!", 1)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Check: list and non-list items:
>>> matrix_divided([[1, 2, 3], "Hey"], 1)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Check: uneven matrix:
>>> matrix_divided([[1, 2, 3], [4, 5, 6, 7]], 3)
Traceback (most recent call last):
...
TypeError: Each row of the matrix must have the same size

Check: mix of ints, floats, and string type:
>>> matrix_divided([[1, "Hey", 3], [4.1, 5, 6.8]], 11)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Check: mix of ints, floats, and bool:
>>> matrix_divided([[0, True, 0], [False, 1, 1]], 11)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Check: mix of ints, floats, and tuple:
>>> matrix_divided([[(10,), 6], [4.4, 5.5]], 11)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

Check: div as string:
>>> matrix_divided([[1, 2, 3], [1, 2, 3]], "X")
Traceback (most recent call last):
...
TypeError: div must be a number

Check: div as bool:
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], True)
Traceback (most recent call last):
...
TypeError: div must be a number

Check: division by zero:
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
Traceback (most recent call last):
...
ZeroDivisionError: division by zero

Check: regular division:
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix
[[1, 2, 3], [4, 5, 6]]

Check: mix of ints and floats:
>>> matrix = [[1, 2.4, 3], [4.1, 5, 6.8]]
>>> matrix_divided(matrix, 11)
[[0.09, 0.22, 0.27], [0.37, 0.45, 0.62]]
>>> matrix
[[1, 2.4, 3], [4.1, 5, 6.8]]

Check: div as float:
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 4.5)
[[0.22, 0.44, 0.67], [0.89, 1.11, 1.33]]
>>> matrix
[[1, 2, 3], [4, 5, 6]]

Check: negative numerators:
>>> matrix = [[-1, -2, -3], [-4, -5, -6]]
>>> matrix_divided(matrix, 3)
[[-0.33, -0.67, -1.0], [-1.33, -1.67, -2.0]]
>>> matrix
[[-1, -2, -3], [-4, -5, -6]]

Check: div as negative:
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, -3)
[[-0.33, -0.67, -1.0], [-1.33, -1.67, -2.0]]
>>> matrix
[[1, 2, 3], [4, 5, 6]]

Check: empty matrix:
>>> matrix = []
>>> matrix_divided(matrix, 1)
[]
>>> matrix
[]

Check: 1xn matrix:
>>> matrix = [[1, 2, 3]]
>>> matrix_divided(matrix, 2)
[[0.5, 1.0, 1.5]]
>>> matrix
[[1, 2, 3]]

Check: nx1 matrix:
>>> matrix = [[1], [2], [3]]
>>> matrix_divided(matrix, 2)
[[0.5], [1.0], [1.5]]
>>> matrix
[[1], [2], [3]]

Check: division by infinity:
>>> matrix_divided(matrix, float('inf'))
[[0.0], [0.0], [0.0]]

Check: division with infinity in numerator:
>>> matrix_divided([[1, float('inf'), 3], [4, 5, 6]], 1)
[[1.0, inf, 3.0], [4.0, 5.0, 6.0]]

Check: division with infinity in numerator and denomenator
>>> matrix_divided([[0, 0, 0], [0, 0, 0]], float('inf'))
[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
