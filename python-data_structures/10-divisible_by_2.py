#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """encuentra todos los elementos de una lista y devuelve una nueva lista
    con True o False si el elemento es divisible por 2 o no
    """
    return [True if i % 2 == 0 else False for i in my_list]