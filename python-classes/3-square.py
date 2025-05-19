#!/usr/bin/python3
"""En este modulo creamos una clase Square"""


class Square():
    """Definicion de clase"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        lado = self.__size
        return (lado * lado)
