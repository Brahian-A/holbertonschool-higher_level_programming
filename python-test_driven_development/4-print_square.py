#!/usr/bin/python3
"""
Modulo que contiene una funcion que imprime un cuadrado"""


def print_square(size):
    "funcion que imprime un cuadrado con el caracter #"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

if __name__ == "__main__":
    print_square(3)
