#!/usr/bin/python3
"""en este modulo cramos una clase con el atributo size """


class Square:
    """ definimos la clase y manejamos errores """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
