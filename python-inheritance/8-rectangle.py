#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Módulo que contiene la clase Rectangle"""


class Rectangle(BaseGeometry):
    """Clase Rectangle que hereda de BaseGeometry y valida ancho y alto."""

    def __init__(self, width, height):
        """Inicializa el objeto Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
