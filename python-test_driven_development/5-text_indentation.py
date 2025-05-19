#!/usr/bin/python3
"""
modulo que define una funcion 
que imprime un texto con 2 saltos de linea
despues de cada '.', '?', y ':'.
"""


def text_indentation(text):
    """
    Funcion que imprime un texto con 2 saltos de linea
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
