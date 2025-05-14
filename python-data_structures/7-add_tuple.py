#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """funcion que suma los primeros 2 elementos de 2 tuplas
    usando un operador ternario o if de una sola linea"""

    tupla_a_1 = tuple_a[0] if len(tuple_a) > 0 else 0
    tupla_a_2 = tuple_a[1] if len(tuple_a) > 1 else 0

    tupla_b_1 = tuple_b[0] if len(tuple_b) > 0 else 0
    tupla_b_2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return [tupla_a_1 + tupla_b_1, tupla_a_2 + tupla_b_2]
