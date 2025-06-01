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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
