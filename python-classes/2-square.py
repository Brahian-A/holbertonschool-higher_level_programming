#!/usr/bin/python3
"""En este modulo creamos una clase con el atributo privado size"""


class Square():
    """Definicion de clase con un atributo privado"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
