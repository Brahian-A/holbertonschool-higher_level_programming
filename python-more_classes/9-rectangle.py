#!/usr/bin/python3
"""creamos una clase"""


class Rectangle:
    """clase Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))

    def my_prrint(self):
        if (self.__height or self.__width) == 0:
            print()
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for i in range(self.__height))

    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
