#!/usr/bin/python3
"funcion que suma 2 variables casteadas a enteros"


def add_integer(a, b=98):
    "funcion que suma variables y maneja errores"
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
