#!/usr/bin/python3

"""se crea la funcion is_same_class("""

def is_same_class(obj, a_class):
    """retorna true si el objeto es una instancia de la clase proporcioada 
        de lo contrario retorna false"""
    return type(obj) is a_class
