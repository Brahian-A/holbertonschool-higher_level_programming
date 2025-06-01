#!/usr/bin/python3
"""creamos la clase Square que hereda de Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """clase que hereda de rectangulo"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        return self.__size * self.__size
