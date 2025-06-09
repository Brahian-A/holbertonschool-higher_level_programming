#!/usr/bin/python3
"""modulo que lee un archivo"""


def read_file(filename=""):
    """funcion accede abre y hace un print del contenido de un archivo"""
    with open(filename, 'r') as contenido:
        print(contenido.read(), end="")
