#!/usr/bin/python3

def no_c(my_string):
    """funcion que devulve una nueva lista sin los
     caracteres c, C """
    new_string = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
