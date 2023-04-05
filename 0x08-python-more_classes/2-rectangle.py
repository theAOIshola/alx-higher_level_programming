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
    
    def area(self):
        """Calculates the area of rectangle"""
        area = self.__width * self.__height
        return area
    
    def perimeter(self):
        """Calculates the perimeter of rectangle"""
        if self.__width or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

my_rectangle = Rectangle(2, 0)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))