Importing the function from the module:
>>> matrix_mul = __import__("100-matrix_mul").matrix_mul

Check: module docstring:
 >>> m = __import__("100-matrix_mul").__doc__
 >>> len(m) > 1
 True

Check: function docstring:
 >>> f = __import__("100-matrix_mul").matrix_mul.__doc__
         >>> len(f) > 1
         True

Check: no args:
 >>> matrix_mul()
 Traceback (most recent call last):
 ...
 TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

Check: one arg:
 >>> matrix_mul([[1, 2], [3, 4]])
 Traceback (most recent call last):
 ...
 TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

Check: too many args:
 >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]])
 Traceback (most recent call last):
 ...
 TypeError: matrix_mul() takes 2 positional arguments but 3 were given

Check: normal use with ints and floats:
 >>> matrix_mul([[1, 2], [3, 4]], [[1.5, 2.5, 3.5], [4.5, 6.5, 7.5]])
 [[10.5, 15.5, 18.5], [22.5, 33.5, 40.5]]

Check: passing m_a as None:
 >>> matrix_mul(None, [[1, 2], [2, 1]])
 Traceback (most recent call last):
 ...
 TypeError: m_a must be a list

Check: passing m_b as None:
 >>> matrix_mul([[1, 2], [2, 1]], None)
 Traceback (most recent call last):
 ...
 TypeError: m_b must be a list

Check: passing empty m_a:
 >>> matrix_mul([], [[1, 2], [2, 1]])
 Traceback (most recent call last):
 ...
 ValueError: m_a can't be empty

Check: passing m_a with empty rows:
 >>> matrix_mul([[], []], [[1, 2], [2, 1]])
 Traceback (most recent call last):
 ...
 ValueError: m_a can't be empty

Check: passing empty m_b:
 >>> matrix_mul([[1, 2], [2, 1]], [])
 Traceback (most recent call last):
 ...
 ValueError: m_b can't be empty

Check: passing m_b with empty rows:
 >>> matrix_mul([[1, 2], [2, 1]], [[]])
 Traceback (most recent call last):
 ...
 ValueError: m_b can't be empty

Check: uneven m_a:
 >>> matrix_mul([[1, 2], [1, 2, 3]], [[1, 2], [2, 1]])
 Traceback (most recent call last):
 ...
 TypeError: each row of m_a must be of the same size

Check: uneven m_b:
 >>> matrix_mul([[1, 2], [2, 1]], [[1, 2], [1, 2, 3]])
 Traceback (most recent call last):
 ...
 TypeError: each row of m_b must be of the same size

Check: string in list in m_a:
 >>> matrix_mul([[1, "Friends"], [2, 1]], [[1, 2], [2, 1]])
 Traceback (most recent call last):
 ...
 TypeError: m_a should contain only integers or floats

Check: string in list in m_b:
 >>> matrix_mul([[1, 2], [2, 1]], [[1, "Friends"], [2, 1]])
 Traceback (most recent call last):
 ...
 TypeError: m_b should contain only integers or floats

Check: mismatching matrices:
 >>> matrix_mul([[1, 1, 1], [1, 1, 1]], [[1, 1], [1, 1,]])
 Traceback (most recent call last):
 ...
 ValueError: m_a and m_b can't be multiplied
