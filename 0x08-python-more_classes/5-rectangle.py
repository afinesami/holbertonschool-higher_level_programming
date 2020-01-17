#!/usr/bin/python3
"""
This is a Rectangle class.
this module contains the class Rectangle.
"""


class Rectangle:
    """Initialize Rectangle object with height and width.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    """
    Calculate area.
    """
    def area(self):
        return (self.width * self.height)

    """
    Calculate perimeter.
    """
    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

    """
    Print Rectangle with #.
    """
    def print(self):
        if (self.width == 0 or self.height == 0):
            print()
            return
        for i in range(self.height):
            for j in range(self.width):
                print("#")
            if i < self.height - 1:
                print()

      def __str__(self):
        out = ""
        if (self.width == 0 or self.height == 0):
            out += "\n"
            return out
        for i in range(self.height):
            for j in range(self.width):
                out += "#"
            if i < self.height - 1:
                out += "\n"
        return out

    """
    Return string.
    """
    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")\n"

    """
    Print the message "Bye rectangle..." when a Rectangle object is deleted.
    """
    def __del__(self):
        print("Bye rectangle...")
