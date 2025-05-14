#!/usr/bin/python3

def max_integer(my_list=[]):
    """funcion que busca el maximo entero dentro de una lista"""
    if len(my_list) == 0:
        return None

    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
