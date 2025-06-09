#!/usr/bin/python3
"""modulo que añade texto a un archivo"""


def append_write(filename="", text=""):
    """funcion que añada texto a un archivo y retorna el archivo"""
    with open(filename, 'a+') as contenido:
        return contenido.write(text)
