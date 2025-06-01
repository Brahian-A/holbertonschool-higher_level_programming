#!/usr/bin/python3
""" definimos la clase """


class BaseGeometry:
    """ clase vacia """
    def area(self):
        """ metodo que no hace nada """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ valida si value es un entero positivo """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

