#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """función que reemplaza todas las ocurrencias de un elemento """
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list
