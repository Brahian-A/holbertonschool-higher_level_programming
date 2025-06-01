#!/usr/bin/python3
"""Modulo que contiene la funcion is_same_class"""


def inherits_from(obj, a_class):
    """retorna True si el objeto es una instancia de la clase si no false"""
    return isinstance(obj, a_class) and type(obj) is not a_class
