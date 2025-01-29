#!/usr/bin/python3
"""en este modulo cramos una clase con el atributo size """
"""comparamos si es un entero o mayor a 0 con su manejo de errores"""


class Square:
    def __init__(self, size=0):
        """" declaramos el atributo size y manejamos errores"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
