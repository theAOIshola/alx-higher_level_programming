#!/usr/bin/python3
"""Definining a Rectangle class"""

class Rectangle:
    """Creates a Rectangle model"""
    def __init__(self, width=0, height=0):
        """Initializes instances of the class"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """Getter for width of the rectangle"""
        return self.__width
    @width.setter
    def width(self, val):
        """Setter for the width of the rectangle"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """Setter for the height of the rectangle"""
        return self.__height
    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val


my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)