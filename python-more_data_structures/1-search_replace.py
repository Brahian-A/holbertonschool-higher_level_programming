#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Función que reemplaza todas las ocurrencias de un elemento."""
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list