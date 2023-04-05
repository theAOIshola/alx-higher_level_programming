def __str__(self):
        """Returns the printable representation of the object
        using the # character
        """
        if self.__width or self.__height == 0:
            return ""
        
        rectangle = []
        for i in range(self.__width):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__width - 1:
                rectangle.append("\n")
        return ("".join(rectangle))