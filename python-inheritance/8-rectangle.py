#!/usr/bin/python3
from base_geometry import BaseGeometry

"""Módulo que contiene la clase Rectangle"""


class Rectangle(BaseGeometry):
    """Clase Rectangle que hereda de BaseGeometry y valida ancho y alto."""

    def __init__(self, width, height):
        """Inicializa el objeto Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
