#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Elimina el elemento en la posición
    dada de la lista y devuelve la lista modificada.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
