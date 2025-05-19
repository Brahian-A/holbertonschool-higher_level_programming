#!/usr/bin/python3
""" Modulo que contiene una funcion que devuelve el maximo de una lista """


def max_integer(list=[]):
    """Funcion que devuelve el maximo de una lista"""
    if len(list) == 0:
        return None
    max_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
    return max_val
