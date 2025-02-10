#!/usr/bin/python3
"""funcion inherits_from"""

def inherits_from(obj, a_class):
    """retorna True si el objeto es una instancia de la clase si no false"""
    return isinstance(obj, a_class) and type(obj) is not a_class