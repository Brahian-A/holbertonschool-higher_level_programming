#!/usr/bin/python3
"""En este modulo creamos una clase Square"""


class Square():
    """Definicion de clase"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = 0
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # Validamos que position sea una tupla de 2 enteros positivos
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size <= 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for e in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
