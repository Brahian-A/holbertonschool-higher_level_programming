#!/usr/bin/python3
"""creamos la clase"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """clase que hereda de rectangulo"""
    def __init__(self, size):
        self.integer_validator(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
