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
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        """Returns the printable representation of the object
        using the # character
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Return a string representation of the Rectangle"""
        rectangle = str(self.__width)
        rectangle += str(self.__height)
        return (rectangle)
        
my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))