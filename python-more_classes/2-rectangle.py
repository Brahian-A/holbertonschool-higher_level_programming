#!/usr/bin/python3
"""Modulo que crea una clase Rectangle"""


class Rectangle():
    """Funcion que crea la clase Rectangle con sus atributos"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width + self.__height) * 2)
