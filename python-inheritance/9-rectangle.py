#!/usr/bin/python3
"""Módulo que contiene la clase Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clase Rectangle que hereda de BaseGeometry y valida ancho y alto."""

    def __init__(self, width, height):
        """Inicializa el objeto Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
