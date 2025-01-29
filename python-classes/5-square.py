#!/usr/bin/python3
""" definimos la clase """


class Square:
    """ manejamos casos de error y el area del square"""
    def __init__(self, size=0):
        self.__size = 0
        self.size = size

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

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        mul = self.__size
        if mul <= 0:
            print()
        for i in range(mul):
            for j in range(mul):
                print("#", end="")
            print()
