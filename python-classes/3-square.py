#!/usr/bin/python3
""" definimos la clase """


class Square:
    """ manejamos casos de error y el area del square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        s = self.__size
        return (s * s)
